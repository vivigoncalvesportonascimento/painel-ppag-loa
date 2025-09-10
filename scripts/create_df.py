from frictionless import Package

def df(datapckage, resource_name):

    package = Package(datapckage)
    resource = package.get_resource(resource_name)
    df = resource.to_pandas()

    return df
