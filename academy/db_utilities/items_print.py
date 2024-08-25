from academy.datamodel.model_base import SqlAlchemyBase


def print_entries(entries: list[SqlAlchemyBase]):
    if entries:
        print(f'{type(entries[0]).__name__} - {len(entries)} items:')
        for item in entries:
            print(f'\t{item}')
    else:
        print(f'No entries found for {type(entries[0]).__name__}')
