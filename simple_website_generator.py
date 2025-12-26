# simple_website_generator.py

# This tool generates a basic HTML website

# Ask user for website details
title = input("Enter your website title: ")
heading = input("Enter your main heading: ")
paragraph = input("Enter a paragraph for your website: ")

# HTML template
html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            text-align: center;
            margin-top: 50px;
            background-color: #f4f4f4;
        }}
        h1 {{
            color: #333;
        }}
        p {{
            font-size: 18px;
            color: #666;
        }}
    </style>
</head>
<body>
    <h1>{heading}</h1>
    <p>{paragraph}</p>
</body>
</html>
"""

# Save to file
file_name = "my_website.html"
with open(file_name, "w") as file:
    file.write(html_content)

print(f"Website generated successfully! Open '{file_name}' in a browser to see it.")
