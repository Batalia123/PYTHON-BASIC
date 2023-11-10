import utils


if __name__ == '__main__':
    args, schema_dict = utils.set_up_parameters()

    utils.generate_records(args, schema_dict)
