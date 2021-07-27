create table if not exists "tokens"
(
    address varchar(42),
    name text,
    symbol text,
    decimals int,
    function_sighashes text[]
);