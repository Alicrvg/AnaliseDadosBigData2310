CREATE DATABASE investimentos_bacen;
use investimentos_bacen;
CREATE TABLE transacoes_correntes (
	data_referencia DATE PRIMARY KEY,
    percentual_pib DECIMAL(10, 2) NOT NULL 
);
select *from transacoes_correntes;

create table idp_mensal(
    data_referencia DATE PRIMARY KEY,
    valor_usd_milhoes DECIMAL(15, 2) NOT NULL
    );
ALTER TABLE idp_mensal 
ADD CONSTRAINT fk_idp_transacoes 
FOREIGN KEY (data_referencia) 
REFERENCES transacoes_correntes(data_referencia);
select *from idp_mensal;

SELECT tc.data_referencia, tc.percentual_pib, idp.valor_usd_milhoes
FROM transacoes_correntes tc
INNER JOIN idp_mensal idp ON tc.data_referencia = idp.data_referencia;

SELECT * 
FROM transacoes_correntes 
WHERE data_referencia BETWEEN '2026-01-01' AND '2026-12-31'
ORDER BY data_referencia ASC;

SELECT MAX(valor_usd_milhoes) AS recorde_idp, MIN(valor_usd_milhoes) AS menor_idp
FROM idp_mensal;

SELECT MIN(percentual_pib) AS maior_deficit_pib
FROM transacoes_correntes;

SELECT 
    AVG(percentual_pib) AS media_pib_periodo,
    SUM(valor_usd_milhoes) AS total_idp_acumulado
FROM transacoes_correntes tc
JOIN idp_mensal idp ON tc.data_referencia = idp.data_referencia;
