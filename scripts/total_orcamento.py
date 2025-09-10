from create_df import df

def total_orcamento_fiscal():
    df_fiscal = df("datapackages/sigplan_2025/datapackage.json", "acoes_planejamento")
    filtered = df_fiscal[df_fiscal["identificador_tipo_acao_cod"].isin([2, 4, 5, 7, 1, 9])]
    total = filtered["vr_meta_orcamentaria_ano0"].sum()
    return total

def total_orcamento_investimento():
    df_fiscal = df("datapackages/sigplan_2025/datapackage.json", "acoes_planejamento")
    filtered = df_fiscal[df_fiscal["identificador_tipo_acao_cod"].isin([8,4])]
    total = filtered["vr_meta_orcamentaria_ano0"].sum()
    return total

