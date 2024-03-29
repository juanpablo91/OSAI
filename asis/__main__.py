#!/usr/bin/env python

from __future__ import annotations

import logging
import os 
import click

# define the cli and group commands 
@click.group()
@click.option('--verbose', is_flag=True, help="Enable verbose logging")
@click.pass_context
def cli(ctx, verbose):
    """commands asis'."""
    # Configuración del registro
    logging.basicConfig(level=logging.INFO if not verbose else logging.DEBUG)
    ctx.obj['VERBOSE'] = verbose




@cli.command(name="new")
@click.argument("project_directory")
@click.pass_context
def new(ctx, project_directory):

    """Create a new MkDocs project."""
    from ASIS.commands import new

    new.new(project_directory)

if __name__ == '__main__':
    # Ejecuta el grupo de comandos
    cli()



