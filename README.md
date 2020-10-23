# pdfix

> Simple command-line tool for propertly rearranging PDF files scanned with printer that doesn't have duplex capabilities.

Problem: a printer without duplex capabilities requires that _all_ of one side of a stack of papers be ran, and then _all_ of the other side be ran. For a six page document, the output becomes:
```
[page 1] [page 3] [page 5] [page 6] [page 4] [page 2]
```

This utility will rearrange them to the proper order.

## Usage

`pdfix example.pdf` will create a file `fixed-example.pdf` in the proper format.
