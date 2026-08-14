{{ config(
    materialized='table',
    schema='batchgold'
) }}

SELECT
    payment_method_id,
    payment_method,
    is_card,
    requires_auth

FROM VALUES
    (1, 'Credit Card', TRUE, TRUE),
    (2, 'Debit Card', TRUE, TRUE),
    (3, 'Digital Wallet', FALSE, FALSE),
    (4, 'Cash', FALSE, FALSE)
AS t(
    payment_method_id,
    payment_method,
    is_card,
    requires_auth
)