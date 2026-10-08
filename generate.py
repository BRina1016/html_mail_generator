import json
import os
from jinja2 import Template


def get_output_filename():
    while True:
        output_filename = input(
            "\n【1. 出力ファイル名】\n"
            "ファイル名を入力してください："
        )

        if output_filename.strip() == "":
            print("ファイル名を入力してください。")
            continue

        if not output_filename.endswith(".html"):
            print("ファイル名は.htmlで終わるようにしてください。")
            continue

        return output_filename


def get_main_text():
    while True:
        main_text = input(
            "\n【2. メール本文】\n"
            "本文を入力してください（改行は \\n）："
        )

        if main_text.strip() == "":
            print("メール本文を入力してください。")
            continue

        return main_text.replace("\\n", "\n")


def get_yes_no(message):
    while True:
        answer = input(message).lower()

        if answer in ["y", "n"]:
            return answer == "y"

        print("yまたはnを入力してください。")


def get_section():
    section = {}

    section["show_text"] = get_yes_no(
        "\n本文を表示しますか？（y/n）："
    )

    if section["show_text"]:
        while True:
            text = input(
                "本文を入力してください（改行は \\n）："
            )

            if text.strip() == "":
                print("本文を入力してください。")
                continue

            section["text"] = text.replace("\\n", "\n")
            break
    else:
        section["text"] = ""

    section["show_button"] = get_yes_no(
        "\nボタンを表示しますか？（y/n）："
    )

    if section["show_button"]:
        section["button_text"] = get_button_text()
        section["button_url"] = get_button_url()
    else:
        section["button_text"] = ""
        section["button_url"] = ""

    return section


def get_sections():
    sections = []

    while True:
        print(f"\n========== セクション{len(sections) + 1} ==========")

        section = get_section()

        # 本文もボタンもない場合はセクションとして追加しない
        if not section["show_text"] and not section["show_button"]:
            print("\n本文もボタンも設定されていないため、")
            print("このセクションは追加しません。")
        else:
            sections.append(section)

        add_next = get_yes_no(
            "\n次のセクションを追加しますか？（y/n）："
        )

        if not add_next:
            break

    return sections


def get_button_url():
    while True:
        button_url = input(
            "\nリンク先URLを入力してください："
        )

        if button_url.startswith("http://") or button_url.startswith("https://"):
            return button_url

        print("URLはhttp://またはhttps://から始めてください。")


def get_button_text():
    while True:
        button_text = input(
            "\nボタンに表示する文字を入力してください："
        )

        if button_text.strip() == "":
            print("ボタンの文言を入力してください。")
            continue

        return button_text


def generate_html(data):
    with open("template/mail.html", "r", encoding="utf-8") as f:
        html = f.read()

    template = Template(html)

    return template.render(data)


def confirm_generation(data, output_filename):
    print("\n================================")
    print("入力内容を確認してください")
    print("================================")

    print(f"\n出力ファイル名：{output_filename}")

    print("\n【メール本文】")
    print(data["main_text"])

    print("\n【セクション一覧】")

    if not data["sections"]:
        print("セクションはありません。")

    for i, section in enumerate(data["sections"], start=1):
        print(f"\n--- セクション{i} ---")

        if section["show_text"]:
            print("本文：表示")
            print(section["text"])
        else:
            print("本文：非表示")

        if section["show_button"]:
            print("ボタン：表示")
            print(f"文言：{section['button_text']}")
            print(f"URL：{section['button_url']}")
        else:
            print("ボタン：非表示")

    while True:
        answer = input(
            "\nこの内容でHTMLを生成しますか？（y/n）："
        ).lower()

        if answer == "y":
            return True

        if answer == "n":
            return False

        print("yまたはnを入力してください。")


def save_html(html, output_filename):
    os.makedirs("output", exist_ok=True)

    output_path = f"output/{output_filename}"

    if os.path.exists(output_path):
        while True:
            answer = input(
                f"\n{output_path}はすでに存在します。"
                "上書きしますか？（y/n）："
            ).lower()

            if answer == "y":
                break

            if answer == "n":
                print("\nHTMLの保存をキャンセルしました。")
                return False

            print("yまたはnを入力してください。")

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html)

    return True

def main():
    print("================================")
    print("      HTMLメール生成ツール")
    print("================================")

    output_filename = get_output_filename()
    main_text = get_main_text()

    sections = get_sections()

    with open("data/mail_data.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    data["main_text"] = main_text
    data["sections"] = sections

    # 入力内容を確認
    if not confirm_generation(data, output_filename):
        print("\nHTMLの生成をキャンセルしました。")
        return

    # HTML生成
    result = generate_html(data)

    # HTML保存
    if not save_html(result, output_filename):
        return

    print("\n================================")
    print("HTMLメールを生成しました。")
    print(f"出力先：output/{output_filename}")
    print("================================")


if __name__ == "__main__":
    main()