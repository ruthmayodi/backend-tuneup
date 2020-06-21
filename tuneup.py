#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tuneup assignment

Use the timeit and cProfile libraries to find bad code.
"""

__author__ = "Ruth Mayodi, ruthmayodi"

import cProfile
import pstats
import functools
import timeit


def profile(func):
    """A cProfile decorator function that can be used to
    measure performance.
    """
    def profile_func(*args, **kwargs):
        profiler = cProfile.Profile()
        try:
            profiler.enable()
            results = func(*args, **kwargs)
            profiler.disable()
            return results
        finally:
            ps = pstats.Stats(profiler).sort_stats(pstats.SortKey.CUMULATIVE)
            ps.print_stats()
    return profile_func
            


def read_movies(src):
    """Returns a list of movie titles."""
    print(f'Reading file: {src}')
    with open(src, 'r') as f:
        return f.read().splitlines()


def is_duplicate(title, movies):
    """Returns True if title is within movies list."""
    for movie in movies:
        if movie == title:
            return True
    return False

@profile
def find_duplicate_movies(src):
    """Returns a list of duplicate movies from a src list."""
    movies = read_movies(src)
    duplicates = []
    while movies:
        movie = movies.pop()
        if movie in movies:
            duplicates.append(movie)
    return duplicates


def timeit_helper(func):
    """Part A: Obtain some profiling measurements using timeit."""
    t = timeit.Timer(stmt=func)
    results = t.repeat(repeat=7, number=3)
    min_value = min([result/3 for result in results])
    print("best time across seven repeats of 3 runs per repeat: ", min_value)
    pass


def main():
    """Computes a list of duplicate movie entries."""
    result = find_duplicate_movies('movies.txt')
    print(f'Found {len(result)} duplicate movies:')
    print('\n'.join(result))


if __name__ == '__main__':
    timeit_helper(main)
