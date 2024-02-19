# Backend Engineering Challenge - Victor Carrillo

Welcome to my repository of the back end challenge. the readme i will divide it into 3 parts

- How to run, build and test
- extra notes of the implementation

## How to run this Repo
### How to install this repo

This repo utilizes [Poetry](https://python-poetry.org/) to install Poetry please [follow their guide](https://python-poetry.org/docs/#installation)

After having Poetry just run `poetry install`

Once it has been installed you can run the CLI by just calling `unbabel-cli --input-file <name-of-file>` for more info on how to run the CLI just
call `unbabel-cli --help` (if for any reason that doesn't work you can call the cli by using `poetry run unbabel-cli`)

### How to build the application?

Run `poetry build` (only build it if you want to install the package into your python (recommend using pipx for it))

### How to test? 

i have installed pytest, all the test are found in the `./test` directory so to run all the test just run `pytest`

### alternative installation

if for some reason you don't want to install it that way you can install it by going through pypi https://pypi.org/project/victor-unbabel-test-cli/
it will run with the name of `unbabel-victor-cli` (i suggest to install it with pipx as i have only tested it that way )


## Notes

Hi, well i have work on this quite fast as i was told the sooner the better. still after i finish i have some after though of the implementation,
So of course there is a lot of room for improvement but i think i convered all the basics of the requirements.

+ I added support for json line and json into the fiels readed because in the example of the sample json there is a json line file and not a json file
so i am not quite certain what should be the expected input so i added value for both options which will read the file differently based on the type of file (described by file .json or .jsonl)

+ I was thinking of using pandas for the calculation which might be better for production as it can allow to do more calculation more organized
to the events list. however due to the requirements i think it was simpler for me to build it manually than just using pandas for it now. but 
for a planning of scalation implementation might have been different

+ I also think that since everything comes organized we could divide the array into chunks and make them process each async which should also optimize way more the code (if the input file are large enough to be relevant) however is an overkill at the moment

## Application Argument:

Example:

```json
{
  "timestamp": "2018-12-26 18:12:19.903159",
  "translation_id": "5aa5b2f39f7254a75aa4",
  "source_language": "en",
  "target_language": "fr",
  "client_name": "airliberty",
  "event_name": "translation_delivered",
  "duration": 20,
  "nr_words": 100
}
```

## Challenge Objective

Your mission is to build a simple command line application that parses a stream of events and produces an aggregated output. In this case, we're interested in calculating, for every minute, a moving average of the translation delivery time for the last X minutes.

If we want to count, for each minute, the moving average delivery time of all translations for the past 10 minutes we would call your application like (feel free to name it anything you like!).

    unbabel_cli --input_file events.json --window_size 10

The input file format would be something like:

    {"timestamp": "2018-12-26 18:11:08.509654","translation_id": "5aa5b2f39f7254a75aa5","source_language": "en","target_language": "fr","client_name": "airliberty","event_name": "translation_delivered","nr_words": 30, "duration": 20}
    {"timestamp": "2018-12-26 18:15:19.903159","translation_id": "5aa5b2f39f7254a75aa4","source_language": "en","target_language": "fr","client_name": "airliberty","event_name": "translation_delivered","nr_words": 30, "duration": 31}
    {"timestamp": "2018-12-26 18:23:19.903159","translation_id": "5aa5b2f39f7254a75bb3","source_language": "en","target_language": "fr","client_name": "taxi-eats","event_name": "translation_delivered","nr_words": 100, "duration": 54}

Assume that the lines in the input are ordered by the `timestamp` key, from lower (oldest) to higher values, just like in the example input above.

The output file would be something in the following format.

```
{"date": "2018-12-26 18:11:00", "average_delivery_time": 0}
{"date": "2018-12-26 18:12:00", "average_delivery_time": 20}
{"date": "2018-12-26 18:13:00", "average_delivery_time": 20}
{"date": "2018-12-26 18:14:00", "average_delivery_time": 20}
{"date": "2018-12-26 18:15:00", "average_delivery_time": 20}
{"date": "2018-12-26 18:16:00", "average_delivery_time": 25.5}
{"date": "2018-12-26 18:17:00", "average_delivery_time": 25.5}
{"date": "2018-12-26 18:18:00", "average_delivery_time": 25.5}
{"date": "2018-12-26 18:19:00", "average_delivery_time": 25.5}
{"date": "2018-12-26 18:20:00", "average_delivery_time": 25.5}
{"date": "2018-12-26 18:21:00", "average_delivery_time": 25.5}
{"date": "2018-12-26 18:22:00", "average_delivery_time": 31}
{"date": "2018-12-26 18:23:00", "average_delivery_time": 31}
{"date": "2018-12-26 18:24:00", "average_delivery_time": 42.5}
```
