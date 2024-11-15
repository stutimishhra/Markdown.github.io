'''import tkinter as tk
from tkinter import filedialog, messagebox
import markdown

# Function to convert markdown to HTML
def convert_to_html():
    try:
        # Get the markdown content from the text box
        markdown_text = text_area.get("1.0", "end-1c")
        
        # Convert markdown to HTML using the markdown library
        html_output = markdown.markdown(markdown_text)
        
        # Show the HTML output in the HTML area
        html_text.delete("1.0", "end")
        html_text.insert("1.0", html_output)
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# Function to save HTML content to a file
def save_html():
    try:
        html_content = html_text.get("1.0", "end-1c")
        
        # Ask the user for the file location to save the HTML content
        file_path = filedialog.asksaveasfilename(defaultextension=".html", filetypes=[("HTML files", "*.html")])
        if file_path:
            with open(file_path, "w") as file:
                file.write(html_content)
            messagebox.showinfo("Success", "HTML file saved successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# Function to open a markdown file
def open_markdown_file():
    try:
        file_path = filedialog.askopenfilename(filetypes=[("Markdown files", ".md;.markdown")])
        if file_path:
            with open(file_path, "r") as file:
                markdown_content = file.read()
            
            # Insert the content into the markdown text area
            text_area.delete("1.0", "end")
            text_area.insert("1.0", markdown_content)
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# Set up the Tkinter root window
root = tk.Tk()
root.title("Markdown to HTML Converter")
root.geometry("850x600")
root.config(bg="#f4f4f9")

# Style settings
font_header = ("Helvetica", 14, "bold")
font_body = ("Helvetica", 12)
bg_pastel_blue = "#d7e3fc"
bg_pastel_pink = "#fbd1d5"
bg_pastel_green = "#d1f7d6"
button_font = ("Helvetica", 12, "bold")

# Create the Markdown Text Area
markdown_label = tk.Label(root, text="Enter Markdown Content:", font=font_header, bg="#f4f4f9", fg="#333")
markdown_label.pack(padx=10, pady=5, anchor="w")
text_area = tk.Text(root, height=12, wrap="word", font=font_body, bg=bg_pastel_blue, fg="#333", relief="solid", borderwidth=1)
text_area.pack(padx=10, pady=5, fill="both", expand=True)

# Create the Convert Button
convert_button = tk.Button(root, text="Convert to HTML", command=convert_to_html, bg="#6c63ff", fg="white", font=button_font, width=20, borderwidth=0, relief="flat")
convert_button.pack(padx=10, pady=10)

# Create the HTML Output Area
html_label = tk.Label(root, text="Generated HTML Output:", font=font_header, bg="#f4f4f9", fg="#333")
html_label.pack(padx=10, pady=5, anchor="w")
html_text = tk.Text(root, height=12, wrap="word", font=font_body, bg=bg_pastel_pink, fg="#333", relief="solid", borderwidth=1)
html_text.pack(padx=10, pady=5, fill="both", expand=True)

# Button Frame
button_frame = tk.Frame(root, bg="#f4f4f9")
button_frame.pack(padx=10, pady=10)

# Create Save Button
save_button = tk.Button(button_frame, text="Save HTML File", command=save_html, bg="#ff6b6b", fg="white", font=button_font, width=20, borderwidth=0, relief="flat")
save_button.grid(row=0, column=0, padx=10, pady=5)

# Create Open File Button
open_button = tk.Button(button_frame, text="Open Markdown File", command=open_markdown_file, bg="#4ecdc4", fg="white", font=button_font, width=20, borderwidth=0, relief="flat")
open_button.grid(row=0, column=1, padx=10, pady=5)

# Run the Tkinter event loop
root.mainloop()'''

import tkinter as tk
from tkinter import filedialog, messagebox
import markdown

# Function to convert markdown to HTML
def convert_to_html():
    try:
        markdown_text = text_area.get("1.0", "end-1c")
        html_output = markdown.markdown(markdown_text)
        html_text.delete("1.0", "end")
        html_text.insert("1.0", html_output)
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# Function to save HTML content to a file
def save_html():
    try:
        html_content = html_text.get("1.0", "end-1c")
        file_path = filedialog.asksaveasfilename(defaultextension=".html", filetypes=[("HTML files", "*.html")])
        if file_path:
            with open(file_path, "w") as file:
                file.write(html_content)
            messagebox.showinfo("Success", "HTML file saved successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# Function to open a markdown file
def open_markdown_file():
    try:
        file_path = filedialog.askopenfilename(filetypes=[("Markdown files", ".md;.markdown")])
        if file_path:
            with open(file_path, "r") as file:
                markdown_content = file.read()
            text_area.delete("1.0", "end")
            text_area.insert("1.0", markdown_content)
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# Function to upload markdown file for conversion
def upload_markdown_file():
    open_markdown_file()
    convert_to_html()

# Set up the Tkinter root window
root = tk.Tk()
root.title("Markdown to HTML Converter")
root.geometry("900x650")
root.configure(bg="#3dbab9")

# Styles
label_font = ("Helvetica", 12, "bold")
text_font = ("Courier", 12)
button_font = ("Helvetica", 10, "bold")
button_bg = "#a2d5c6"
button_fg = "white"

# Markdown Input Area
markdown_label = tk.Label(root, text="Enter Markdown Content:", font=label_font, bg="#faf3e0")
markdown_label.pack(pady=(15, 5), anchor="w", padx=15)
text_area = tk.Text(root, height=15, wrap="word", font=text_font, bg="#e6e6fa", fg="#333333")
text_area.pack(padx=15, pady=5, fill="both", expand=True)

# Button Frame
button_frame = tk.Frame(root, bg="#faf3e0")
button_frame.pack(pady=10)

# Convert, Upload, and Save Buttons
convert_button = tk.Button(button_frame, text="Convert to HTML", command=convert_to_html, bg=button_bg, fg=button_fg, font=button_font)
convert_button.grid(row=0, column=0, padx=5, pady=5)
upload_button = tk.Button(button_frame, text="Upload Markdown File", command=upload_markdown_file, bg="#fcbf49", fg="white", font=button_font)
upload_button.grid(row=0, column=1, padx=5, pady=5)
save_button = tk.Button(button_frame, text="Save HTML File", command=save_html, bg="#457b9d", fg="white", font=button_font)
save_button.grid(row=0, column=2, padx=5, pady=5)

# HTML Output Area
html_label = tk.Label(root, text="Generated HTML Output:", font=label_font, bg="#faf3e0")
html_label.pack(pady=(15, 5), anchor="w", padx=15)
html_text = tk.Text(root, height=15, wrap="word", font=text_font, bg="#a2a2d0", fg="#333333")
html_text.pack(padx=15, pady=5, fill="both", expand=True)

# Run the Tkinter event loop
root.mainloop()
