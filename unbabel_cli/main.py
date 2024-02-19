from pathlib import Path
import typer

from typing_extensions import Annotated
from unbabel_cli.utils.delivery_time import process_avg_delivery_time

from unbabel_cli.utils.read_events import read_event

# This is the definition of the CLI
app = typer.Typer()


# This mean to use the main function as the entry point of the CLI
@app.command()
def main(
    input_file: Annotated[
        Path,
        typer.Option("--input-file", "-i", exists=True, help="Path of file to read"),
    ],
    window_size: Annotated[
        int, typer.Option(help="Average windows for the calculations")
    ] = 10,
    output_file: Annotated[
        Path,
        typer.Option(help="Path of file to write the output"),
    ] = "output.jsonl",
    delete_file_after: Annotated[
        bool,
        typer.Option(
            "--delete-file-after/", "-d/", help="Delete the file after the execution"
        ),
    ] = False,
):
    """
    prints and write into a file the moving average of the translation delivery time for the last X minutes.
    """

    events = read_event(input_file)
    process_avg_delivery_time(events, window_size, output_file=output_file)

    if delete_file_after:
        output_file.unlink()
        return
    print(f"Results written to {output_file}")
