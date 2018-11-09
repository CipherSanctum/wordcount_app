# A character filtering word count app for Django 2.x

## DESCRIPTION:

This word count app removes characters you don't want *(commas, periods, semicolons, colons, apostrophes, etc.)*. That way, a person
who types *"hi"* and *"hi,"* into the *<textarea>* will get a count of 2 for *"hi"* instead of 1 for each variation.

**If you want any character removed:** Add the single string you don't want into the *delete_values* list.

**If your goal wasn't to count words, but filter them:** You could use this as a springboard and modify the function to filter certain words. Doing so would simplify the function far more.

### EXAMPLE:

No signup or login required: https://pwnsaucedesigns.com/wordcount_app/
