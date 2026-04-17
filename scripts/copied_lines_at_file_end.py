import argparse
from typing import Sequence, IO


def fix_file(file_obj: IO[str]) -> int:
    # Read the entire file content
    content = file_obj.readlines()
    modified = False
    # if the file is empty, return immediately
    if not content:
        return 0
    # go through file from the end to the beginning
    last_line_nr = len(content) - 1
    if content[last_line_nr].strip() == "":
        # if the last line is empty, ignore it
        last_line_nr -= 1

    if last_line_nr < 1:
        # if the file has only one line, return immediately
        return 0

    # if the last line is the same as the previous line, remove it
    while content[last_line_nr].strip() == content[last_line_nr - 1].strip():
        modified = True
        content.pop(last_line_nr)
        last_line_nr -= 1
        if last_line_nr < 1:
            break

    if modified:
        # Move the file pointer to the beginning of the file
        file_obj.seek(0)
        # Write the modified content back to the file
        file_obj.writelines(content)
        # Truncate the file to the new length
        file_obj.truncate()
        return 1
    else:
        return 0


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("filenames", nargs="*", help="Filenames to fix")
    args = parser.parse_args(argv)

    retv = 0

    for filename in args.filenames:
        # Read as binary so we can read byte-by-byte
        with open(filename, "r+") as file_obj:
            ret_for_file = fix_file(file_obj)
            if ret_for_file:
                print(f"Fixing {filename}")
            retv |= ret_for_file

    return retv


if __name__ == "__main__":
    raise SystemExit(main())
