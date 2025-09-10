from frictionless import Package

package = Package("datapackages/sigplan_2025/datapackage.json")
resource = package.get_resource("acoes_planejamento")
df = resource.to_pandas()

# Filter rows where identificador_tipo_acao_cod is in the list
filtered = df[df["identificador_tipo_acao_cod"].isin([2, 4, 5, 7, 1, 9])]

# Sum the column
total = filtered["vr_meta_orcamentaria_ano0"].sum()
