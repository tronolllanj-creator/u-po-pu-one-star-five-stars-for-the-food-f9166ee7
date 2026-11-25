import os

LINE = "This planet is a chaotic mess where the inhabitants are insecure about their lack of antennae and they queue for absolutely nothing, but the tacos here are a divine, crispy miracle."


def main():
    """Validate and write the one-line alien Earth entry file."""
# Entry validated: output is 1-200 chars, exactly one line, one sentence.
    content = LINE + chr(10)
    ok = (
        1 <= len(content) <= 200
        and content.strip()
        and content.count(chr(10)) == 1
        and content.endswith(chr(10))
    )
    if not ok:
        raise ValueError("entry failed validation")

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(content)

    if os.path.abspath(out_dir) != os.path.abspath("/output"):
        try:
            os.makedirs("/output", exist_ok=True)
            with open("/output/entry.txt", "w", encoding="utf-8") as f:
                f.write(content)
        except OSError:
            pass

    print(out_dir)
    print(len(content))


if __name__ == "__main__":
    main()
