#!/usr/bin/env python3
"""
Chinese Text to Pinyin Converter
Reads a Chinese text file and adds pinyin above characters
Preserves original formatting exactly
"""

import argparse
from pypinyin import pinyin, Style
import os

def add_pinyin_preserve_format(chinese_text):
    """
    Add pinyin above Chinese characters while preserving all original content exactly
    """
    lines = chinese_text.split('\n')
    result_lines = []
    
    for line in lines:
        # Process line character by character to maintain perfect alignment
        pinyin_line = ""
        original_line = ""
        
        i = 0
        while i < len(line):
            char = line[i]
            
            if '\u4e00' <= char <= '\u9fff':  # Chinese character
                # Get pinyin for this character
                py = pinyin(char, style=Style.TONE, heteronym=False)[0][0]
                # Add pinyin to pinyin line
                pinyin_line += py.ljust(len(char) + 2)  # Add some padding
                # Add original character to original line
                original_line += char.ljust(len(char) + 2)
            else:
                # For non-Chinese characters (spaces, punctuation, etc.)
                # Add same character to both lines
                pinyin_line += ' ' * len(char)  # Space in pinyin line
                original_line += char  # Original character in original line
            
            i += 1
        
        # Only add pinyin line if the original line had Chinese characters
        if any('\u4e00' <= char <= '\u9fff' for char in line):
            result_lines.append(pinyin_line.rstrip())  # Remove trailing spaces from pinyin line
        
        result_lines.append(line)  # Add original line
    
    return '\n'.join(result_lines)


def add_pinyin_preserve_format_new(chinese_text):
    """
    Improved method to add pinyin above Chinese characters while preserving formatting
    """
    from pypinyin import pinyin, Style, lazy_pinyin
    
    lines = chinese_text.split('\n')
    result_lines = []
    
    for line in lines:
        if not line.strip():
            result_lines.append(line)
            continue
            
        # Identify Chinese characters and their positions
        pinyin_parts = []
        original_parts = []
        
        i = 0
        while i < len(line):
            char = line[i]
            
            if '\u4e00' <= char <= '\u9fff':  # Chinese character
                # Get pinyin for this character
                py = pinyin(char, style=Style.TONE, heteronym=False)[0][0]
                pinyin_parts.append((i, py))
            i += 1
        
        # Build the pinyin line based on original line structure
        pinyin_line = [' '] * len(line)
        original_line = list(line)
        
        for pos, py in pinyin_parts:
            # Place pinyin at the correct position
            # We'll put the pinyin in a separate line above the original
            pass
        
        # Instead, let's build character-by-character
        pinyin_str = ""
        for char in line:
            if '\u4e00' <= char <= '\u9fff':
                py = pinyin(char, style=Style.TONE, heteronym=False)[0][0]
                pinyin_str += py + "  "  # Add padding
            else:
                # For non-Chinese characters, add equivalent spaces in pinyin line
                pinyin_str += " " * len(char)  # This is just 1 for single char
        
        # Actually, we need a different approach - let's map each original character position
        # to either a pinyin string or a space
        pinyin_line = ""
        char_idx = 0
        
        for char in line:
            if '\u4e00' <= char <= '\u9fff':  # Chinese character
                py = pinyin(char, style=Style.TONE, heteronym=False)[0][0]
                pinyin_line += py.ljust(len(char) + 2)  # Pad with spaces to align
            else:
                pinyin_line += " " * len(char)  # Space for non-Chinese char
        
        # Only add pinyin line if there were Chinese characters in the line
        if any('\u4e00' <= char <= '\u9fff' for char in line):
            result_lines.append(pinyin_line.rstrip())
        
        result_lines.append(line)
    
    return '\n'.join(result_lines)


def add_pinyin_preserve_format_corrected(chinese_text):
    """
    Correct method to add pinyin above Chinese characters while preserving formatting
    """
    lines = chinese_text.split('\n')
    result_lines = []
    
    for line in lines:
        if not line.strip():
            result_lines.append(line)
            continue
            
        # Create pinyin and character mapping
        pinyin_chars = []
        original_chars = []
        
        for char in line:
            if '\u4e00' <= char <= '\u9fff':  # Chinese character
                py = pinyin(char, style=Style.TONE, heteronym=False)[0][0]
                pinyin_chars.append(py)
                original_chars.append(char)
            else:  # Non-Chinese character (punctuation, space, etc.)
                pinyin_chars.append(' ')  # Space in pinyin line
                original_chars.append(char)  # Original character
        
        # Now build the pinyin line ensuring proper spacing
        pinyin_line = ""
        original_line = ""
        
        for i, char in enumerate(line):
            if '\u4e00' <= char <= '\u9fff':  # Chinese character
                py = pinyin(char, style=Style.TONE, heteronym=False)[0][0]
                pinyin_line += py.ljust(6)  # Pad pinyin to align with Chinese character
                original_line += char.ljust(6)  # Pad original character too
            else:  # Non-Chinese character
                pinyin_line += char  # Same character in pinyin line
                original_line += char  # Same character in original line
        
        # Adjust spacing to match original line length
        if any('\u4e00' <= c <= '\u9fff' for c in line):
            result_lines.append(pinyin_line.rstrip())
        result_lines.append(original_line.rstrip())
    
    return '\n'.join(result_lines)


def add_pinyin_preserve_format_final(chinese_text):
    """
    Final corrected method to add pinyin above Chinese characters while preserving formatting
    """
    from pypinyin import pinyin, Style
    
    lines = chinese_text.split('\n')
    result_lines = []
    
    for line in lines:
        if not line.strip():
            result_lines.append(line)
            continue
            
        # Build pinyin line by processing each character
        pinyin_line = ""
        char_pos = 0
        
        while char_pos < len(line):
            char = line[char_pos]
            
            if '\u4e00' <= char <= '\u9fff':  # Chinese character
                py = pinyin(char, style=Style.TONE, heteronym=False)[0][0]
                # Add pinyin with proper spacing to match original character width
                pinyin_line += py.ljust(2)  # Use 2 spaces to separate from next
            else:  # Non-Chinese character
                # Add the same character to pinyin line (typically space or punctuation)
                pinyin_line += " " * len(char)  # This will be just 1 space for single char
            
            char_pos += 1
        
        # Only add pinyin line if there are Chinese characters in the original line
        if any('\u4e00' <= c <= '\u9fff' for c in line):
            result_lines.append(pinyin_line.rstrip())
        
        result_lines.append(line)
    
    return '\n'.join(result_lines)


def add_pinyin_preserve_format_best(chinese_text):
    """
    Best approach: Process each line to add pinyin preserving exact formatting
    """
    from pypinyin import pinyin, Style
    
    lines = chinese_text.split('\n')
    result_lines = []
    
    for line in lines:
        if not line.strip():
            result_lines.append(line)
            continue
            
        # Identify all Chinese characters and their positions
        ch_chars = []
        ch_positions = []
        
        for i, char in enumerate(line):
            if '\u4e00' <= char <= '\u9fff':
                ch_chars.append(char)
                ch_positions.append(i)
        
        if not ch_chars:
            # No Chinese characters in this line, just add the original line
            result_lines.append(line)
            continue
        
        # Get pinyin for all Chinese characters
        pinyin_list = pinyin(''.join(ch_chars), style=Style.TONE, heteronym=False)
        pinyin_values = [p[0] for p in pinyin_list]
        
        # Create the pinyin line by mapping pinyin values back to their positions
        pinyin_line = [' '] * len(line)  # Start with all spaces
        
        for pos, py_val in zip(ch_positions, pinyin_values):
            # Insert pinyin value at the correct position
            # We need to be careful about character width
            py_len = len(py_val)
            line_len = len(line)
            
            # Place pinyin value at the position, making sure not to exceed line length
            end_pos = min(pos + py_len, line_len)
            pinyin_line[pos:end_pos] = py_val[:end_pos-pos]
            
            # For better alignment, add extra spaces if needed
            if end_pos < line_len and line[end_pos] != ' ':
                # Add a separator between pinyin elements
                pass
        
        # Convert pinyin line back to string
        pinyin_str = ''.join(pinyin_line)
        
        # Add the pinyin line and then the original line
        result_lines.append(pinyin_str)
        result_lines.append(line)
    
    return '\n'.join(result_lines)


def add_pinyin_preserve_format_working(chinese_text):
    """
    Working approach to add pinyin above Chinese characters while preserving formatting
    """
    from pypinyin import pinyin, Style
    
    lines = chinese_text.split('\n')
    result_lines = []
    
    for line in lines:
        if not line.strip():
            result_lines.append(line)
            continue
        
        # Create character mapping
        pinyin_mapping = []
        
        for i, char in enumerate(line):
            if '\u4e00' <= char <= '\u9fff':  # Chinese character
                py = pinyin(char, style=Style.TONE, heteronym=False)[0][0]
                pinyin_mapping.append((i, py))
        
        if not pinyin_mapping:  # No Chinese characters in this line
            result_lines.append(line)
            continue
        
        # Create pinyin line with proper spacing
        pinyin_line = [' '] * len(line)
        
        # Place pinyins at their corresponding positions
        for pos, py in pinyin_mapping:
            py_len = len(py)
            # Place pinyin starting at the original character position
            for j in range(min(py_len, len(line) - pos)):
                pinyin_line[pos + j] = py[j]
        
        # Add pinyin line and original line
        result_lines.append(''.join(pinyin_line))
        result_lines.append(line)
    
    return '\n'.join(result_lines)


def add_pinyin_preserve_format_optimized(chinese_text):
    """
    Proper approach to add pinyin above Chinese characters while preserving formatting.
    Each Chinese character gets its own pinyin on the line above.
    """
    from pypinyin import pinyin, Style
    
    lines = chinese_text.split('\n')
    result_lines = []
    
    for line in lines:
        if not line.strip():
            result_lines.append(line)
            continue
        
        # Check if line has any Chinese characters
        has_chinese = any('\u4e00' <= char <= '\u9fff' for char in line)
        if not has_chinese:
            result_lines.append(line)
            continue
        
        # Get pinyin for Chinese characters while preserving positions
        # We need to process this character by character
        pinyin_line = ""
        i = 0
        while i < len(line):
            char = line[i]
            if '\u4e00' <= char <= '\u9fff':  # Chinese character
                # Get the pinyin for this character
                py = pinyin(char, style=Style.TONE, heteronym=False)[0][0]
                # Add pinyin with padding to align properly
                pinyin_line += py + "  "  # Add padding to separate from next pinyin
            else:
                # For non-Chinese characters, add the same character or a space
                # If it's a punctuation, we might want to add a longer space to keep alignment
                if char.isspace():
                    pinyin_line += char  # Keep spaces in pinyin line too
                else:
                    # For punctuation, add spaces for alignment
                    pinyin_line += " " * len(char)
            i += 1
        
        result_lines.append(pinyin_line.rstrip())
        result_lines.append(line)
    
    return '\n'.join(result_lines)


def process_file(input_file, output_file=None):
    """
    Process input file and generate output with pinyin
    """
    try:
        # Read input file
        with open(input_file, 'r', encoding='utf-8') as f:
            chinese_text = f.read()
        
        # Generate pinyin output
        pinyin_text = add_pinyin_preserve_format_optimized(chinese_text)
        
        # Determine output filename
        if output_file is None:
            name, ext = os.path.splitext(input_file)
            output_file = f"{name}_pinyin{ext}"
        
        # Write output file
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(pinyin_text)
        
        print(f"Successfully processed: {input_file}")
        print(f"Output saved as: {output_file}")
        
        # Also print to console
        print("\nPreview:")
        print("-" * 40)
        print(pinyin_text)
        print("-" * 40)
        
    except FileNotFoundError:
        print(f"Error: Input file '{input_file}' not found.")
    except Exception as e:
        print(f"Error processing file: {e}")

def main():
    parser = argparse.ArgumentParser(description='Add pinyin above Chinese characters in a text file')
    parser.add_argument('input_file', help='Input Chinese text file')
    parser.add_argument('-o', '--output', help='Output file (optional)')
    
    args = parser.parse_args()
    
    process_file(args.input_file, args.output)

if __name__ == "__main__":
    # If no command line arguments, prompt user
    import sys
    if len(sys.argv) == 1:
        input_file = input("Enter the path to your Chinese text file: ")
        output_file = input("Enter output file path (or press Enter for auto-generated name): ").strip()
        if not output_file:
            output_file = None
        process_file(input_file, output_file)
    else:
        main()