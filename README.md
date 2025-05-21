###Habit Analyzer###

A simple, focused system for analyzing habit records, designed to turn raw data into actionable insights.

###Technologies Used###


Python 3.x

Standard libraries (collections, file handling)

Modular architecture with separate files: parser.py, analyzer.py, reporter.py

###Project Purpose###

Captures, processes, and analyzes daily activity data stored in a log file (data/logs.txt). The system:

Reads entries formatted as: date, type, value

Groups and counts occurrences by type

Calculates sums and averages of values by date and activity type

Produces clear, organized reports for easy tracking and decision-making

This project serves as a foundation for automating and monitoring habits, easily adaptable for other simple periodic data analysis needs.

###File Structure###

parser.py — Reads and parses the log file, transforming data into a structure ready for analysis.

analyzer.py — Performs data analysis, counting and summarizing relevant information.

reporter.py — Generates consolidated reports, showing sums and averages grouped by date and activity type.

###How to Use###

Make sure the file data/logs.txt is properly formatted with lines like:

##bash##

YYYY-MM-DD, type, value

##Example:##

2025-05-20, sleep, 7.5

2025-05-20, workout, 1.0


Run the main script to see the summary and full report:

bash:


cd habit_analyzer

$ PYTHONUTF8=1 python src/analyzer.py

###Contact###


Professional email: victor.de.alcantara.bueno@gmail.com

Discord: index_salazar

Feedback

Constructive criticism, questions, and suggestions are essential for this project's growth. Feel free to contribute or open issues.

