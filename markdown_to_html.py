import markdown
import os

def convert_md_to_html(md_text):
    return markdown.markdown(md_text)

def main():
    print("📝 Markdown to HTML Converter")
    filename = input("Enter the name of your markdown file (e.g., `example.md`): ").strip()
    
    if not filename.endswith(".md"):
        print("Error: Please provide a valid `.md` file.")
        return

    if not os.path.exists(filename):
        print("Error: File not found.")
        return

    with open(filename, "r") as md_file:
        md_text = md_file.read()
        html_output = convert_md_to_html(md_text)

    output_filename = filename.replace(".md", ".html")
    with open(output_filename, "w") as html_file:
        html_file.write(html_output)

    print(f"✅ Converted HTML saved to `{output_filename}`")

if __name__ == "__main__":
    main()
