"""
Functions related to the installation of a nodejs project, containing the tailwind dependency, as well as generating the css
"""
import os
from subprocess import run as exec

empty_tailwind_config = """
// tailwind.config.js
module.exports = {
  purge: [],
  darkMode: false, // or 'media' or 'class'
  theme: {
    extend: {},
  },
  variants: {},
  plugins: [],
}
"""

def install_tailwind_generator():
    completed_node_version = exec(["node", "-v"], capture_output=True)
    if (completed_node_version.returncode != 0):
        print("nodejs not found")
        exit(1)
    completed_npm_version = exec(["npm", "help"], capture_output=True)
    if (completed_npm_version.returncode != 0):
        print("Error running npm")
        exit(1)
    
    # Generate a folder, and put the thingy in it
    tailwind_dir = os.path.join(os.getcwd(), "tailwind_generator")
    try:
        # Create the base directory
        os.mkdir(tailwind_dir)
        # Create empty package.json
        print("Initializing tailwind")
        init_tailwind = exec(["npm init -y"], shell=True, cwd=tailwind_dir)
        if (init_tailwind.returncode != 0):
            print("Error initializing package.json")
            exit(1)
        # Install packages
        packages_for_tailwind = ["tailwindcss@latest", "postcss@latest", "autoprefixer@latest"]
        install_packages = exec(["npm install tailwindcss@latest postcss@latest autoprefixer@latest"], shell=True, cwd=tailwind_dir)
        if install_packages.returncode != 0:
            print("Error installing packages")
            exit(0)
        with open(os.path.join(tailwind_dir, "tailwind.config.js"), "w") as tailwind_config_file:
            tailwind_config_file.write(empty_tailwind_config)
    except FileExistsError:
        pass


def generate_tailwind_css():
        # Generate a folder, and put the thingy in it
    tailwind_dir = os.path.join(os.getcwd(), "tailwind_generator")
    original_dir = os.getcwd()
    if not os.path.isfile(os.path.join(original_dir,"tailwind.css")):
        print("Regenerating tailwind")
        generate_tailwind_css = exec(["npx tailwindcss -o {}".format(os.path.join(original_dir,"tailwind.css"))], shell=True, cwd=tailwind_dir)