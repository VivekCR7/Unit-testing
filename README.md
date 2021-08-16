# Company Master

This project is more of a data project, data visualization. The main aim of the project is
to convert the raw open data plots, that tells a story on the state of Company registration.
One important thing in this project is, there is no use of built-in libraries for transforming
the data, libraries like pandas are not used in this project.

<br>

## Dataset

raw data which is .csv file, it's the real world data of company registration in the state of maharashtra.
below is the link you can download the data from there.

Two dataset has been used for this project:

| Dataset | Link |
| --- | --- |
| Company Master data of Maharashtra | https://tinyurl.com/94s2nax3 |
| District vs zip data | https://tinyurl.com/39tauusa |

<br>

## Run Locally

Clone the project

```bash
~ git clone https://github.com/VivekCR7/Unit-testing.git
```

Go to the project directory

```bash
~ cd unit-testing
```

Make a directory dataset and then move the downloaded data in that directory using terminal or from gui.

```bash
~ mkdir dataset
~ mv downloads/Maharashtra.csv ./dataset/
~ mv downloads/district_zip.csv ./dataset/
```

create virtual enviornment

```bash
~ pip3 install virtualenv
~ virtualenv venv
```

activate the virtual enviornment

```bash
~ source venv/bin/activate
```
once the virtual enviornment is activated there will be a (venv) before the tilde(~) sign in your terminal, means you are good to go.

```bash
(venv) ~ pwd
```

Once virtual enviornment is on, install all the dependencies

```bash
(venv) ~ pip3 install -r requirements.txt
```

Check for the pep8 standard using flake8, if there is no error while running the below code then it will show nothing but if there is an error it will show on which line the error is

```bash
(venv) ~ cd tasks
(venv) ~ flake8 transform.py
(venv) ~ flake8 histogram_of_authorized_cap.py
(venv) ~ flake8 barplot.py
(venv) ~ flake8 bar_chart_for_year_2015.py
(venv) ~ flake8 grouped_bar_plot.py
(venv) ~ flake8 data.py
(venv) ~ flake8 test_data.py
```

To run the unit-testing file

```bash
python3 test_data.py
```

```bash
......
----------------------------------------------------------------------
Ran 6 tests in 0.000s

OK
```

Above is the output of the unit testing.

## Author

- [@Vivek Dubey]()

  
