import pandas as pd
import matplotlib.pyplot as plt


def carga(path, sep=None):
    if sep:
        return pd.read_csv(path, sep)
    else:
        return pd.read_csv(path)


def convert_point_coma(df,column):
    df[column] = df[column].apply(lambda x: x.replace(',', '.'))
    df[column] = df[column].astype(float)
    return df


def pre_procesado_1(df):
    df['CLUSTER'] = df['CLUSTER'].apply(lambda x: x.replace('CLUSTER ', ''))
    df['CLUSTER'] = df['CLUSTER'].astype(int)
    df = convert_point_coma(df, 'Consumo / t km')
    df = convert_point_coma(df, 't. marcha lenta/ t. motor ligado')
    df = convert_point_coma(df, 'Custo / km')
    df = convert_point_coma(df, 't. movimento / t. produtivo disponivel')
    df = convert_point_coma(df, 'Excesso RPM / km')
    df = convert_point_coma(df, '(%) operacao faixa economica')
    df = convert_point_coma(df, 'n de excessos de velocidade / 1000 km')
    df = convert_point_coma(df, 't. excesso de velocidade / t. movimento')
    df = convert_point_coma(df, 'Emissao de CO2 (kg CO2 / t km)')
    df = convert_point_coma(df, 'Emissao de Nox (g Nox / t km)')
    df = convert_point_coma(df, 'Emissao de MP (g MP  / t km)')
    return df


if __name__ == '__main__':
    df = carga('data/Datos_prueba.csv', '\t')
    df = pre_procesado_1(df)
    # fig, (ax1, ax2) = plt.subplots(1, 2)
    fig = plt.figure()
    ax = fig.add_subplot(111)

    #df.plot(kind='box')
    #df.boxplot(column=['Consumo / t km'])
    # df['Consumo / t km'].plot.box(ax=ax1)
    # df['Custo / km'].plot.box(ax=ax2)
    df.groupby('CLUSTER')['Consumo / t km'].mean().plot(kind='barh')
    # df.groupby('PLACAS').plot(x='CLUSTER', y='Consumo / t km', ax=ax, legend=True)

    plt.show()
    print(df.dtypes)
