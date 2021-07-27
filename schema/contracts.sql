create table if not exists "contracts"
(
    address varchar(42),
    bytecode text,
    function_sighashes text[]
);