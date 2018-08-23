#!/usr/bin/env python3

import argparse
import logging
import re
import sys


def build_page(args, words):
    tail = len(words) % args.columns
    height = int(len(words) / args.columns)
    if tail != 0:
        height += 1
    addition = args.columns * height - len(words)
    stub = re.sub(r'\S', '', words[0])
    words += [stub for _ in range(addition)]
    rows = []
    for y_idx in range(height):
        cur_row = ''
        for x_idx in range(args.columns):
            if cur_row:
                cur_row += args.separator
            idx = y_idx + x_idx * height
            cur_row += words[idx]
        rows.append(cur_row)
    return rows


def process_input_file(args):
    pages = []
    if args.infile:
        with open(args.infile) as fd:
            pages = iterate_over_input(args, fd)
    else:
        pages = iterate_over_input(args, sys.stdin)
    return pages


def iterate_over_input(args, fd):
    pages = []
    words = []
    for l in fd.readlines():
        words.append(l.rstrip())
        if len(words) >= args.columns * args.rows:
            page = build_page(args, words)
            pages.append(page)
            words = []
    if len(words) > 0:
        page = build_page(args, words)
        pages.append(page)
    return pages


def write_output_file(args, pages):
    if args.outfile:
        with open(args.outfile, 'w') as fd:
            write_pages(args, pages, fd)
    else:
        write_pages(args, pages, sys.stdout)


def write_pages(args, pages, fd):
    for page in pages:
        for row in page:
            fd.writelines(row + "\n")
        fd.writelines(args.page_separator)


def main(args):
    pages = process_input_file(args)
    write_output_file(args, pages)


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--infile')
    parser.add_argument('-o', '--outfile')
    parser.add_argument('-c', '--columns', default=4)
    parser.add_argument('-r', '--rows', default=64)
    parser.add_argument('-s', '--separator', default="\t")
    parser.add_argument('-p', '--page_separator', default="\n")
    parser.add_argument('-d', '--debug', default='info')
    return parser.parse_args()


if __name__ == '__main__':
    arguments = get_args()
    debug_level = arguments.debug.upper()
    logging.basicConfig(format='%(asctime)s %(message)s', level=debug_level)
    main(arguments)
