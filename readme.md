# Personal Information

- Full Name: Rafanomezantsoa Ny Aina Herilala
- Email: hei.herilala@gmail.com
- STD Reference: STD21108

## Using the Code

This code is designed to check URLs using multiple threads. Here are the steps to use it:

1. **Prerequisites:** Make sure you have Python installed on your system.

2. **library:** Make sure you have Python library installed on your system.
    - concurrent
    - requests
    - sys
    - os
    - threading

3. **Downloading the code:** Download the code from the Git repository or copy it locally to your machine.

4. **Preparing the URLs:** Prepare a text file containing the URLs you want to check. Each URL should be on a separate line.

5. **Running the script:** Open a terminal or command prompt, then run the Python script by specifying the necessary arguments:
    - Utilisation: 
python check_end_point.py path_to_file number_of_threads url_path
        - `path_to_file`: Path to the file containing the list of dir.
        - `number_of_threads`: Number of threads to use for the check (when to exceed the maximum recommended number of threads by your system, the maximum will be used).
        - `url_path`: Base path of the URLs to check.
    - ***example of working use:*** 
`python check_end_point.py dir_list.txt 30 https://www.facebook.com `

6. **Analyzing the results:** The script will check each URL and display those that return a response with status code 200.

Feel free to contact the author in case of any questions or issues encountered while using the code.
