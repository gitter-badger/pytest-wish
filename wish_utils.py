
import importlib
import logging

DISTRIBUTION_BLACKLIST = []


def import_modules(distributions):
    distribution_modules = []
    for distribution in distributions:
        if distribution.project_name in DISTRIBUTION_BLACKLIST:
            continue
        module_names = distribution.get_metadata('top_level.txt').splitlines()
        for module_name in module_names:
            try:
                importlib.import_module(module_name)
            except:
                logging.info("Can't import top_level %r from %r", module_name, distribution.key)
        distribution_requirement = str(distribution.as_requirement())
        distribution_modules.append((distribution_requirement, module_names))
    return distribution_modules