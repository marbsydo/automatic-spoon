import glob
import os
import shutil
import fileinput
import sys

if __name__ == "__main__":
    
    # TODO: Sort out generating an "index.html"

    out_dir = "webapp/www"
    pages_dir = "pages"
    template_html = "template.html"

    # Change to one directory below `out_dir` directory
    os.chdir("..")

    # Delete contents of output directory
    shutil.rmtree("{}".format(out_dir), ignore_errors=True)

    # Copy static files into place
    shutil.copytree("static/", "{}/static/".format(out_dir)) 

    # Change to directory where site pages are
    os.chdir("{}".format(pages_dir))
    filenames = glob.glob("*.html")
    if not template_html in filenames:
        print("Missing {}".format(template_html))
        exit()
    filenames.remove(template_html)
    os.chdir("..")
 
    for filename in filenames:

        # Copy template and rename with page name
        shutil.copy2("{}/{}".format(pages_dir, template_html), "{}/{}".format(out_dir, filename))

        # Read contnts of page
        with open("{}/{}".format(pages_dir, filename)) as fp:
            page_content = fp.read()

        # Split content into lines, and remove last line which is always blank
        page_content = page_content.split("\n")
        del page_content[-1]

        for line in fileinput.input("{}/{}".format(out_dir, filename), inplace=True):
            if line.strip() == "{{content}}":
                # Replace a line that just contains {{content}} with page content
                indent = line.find("{")
                indent_str = " " * indent
                for content_line in page_content:
                    sys.stdout.write(indent_str + content_line + "\n")
            elif "{{page}}" in line:
                # Replace {{page}} with the page name
                page_name = filename.split('.')[0]
                sys.stdout.write(line.replace("{{page}}", page_name))
            else:
                sys.stdout.write(line)
