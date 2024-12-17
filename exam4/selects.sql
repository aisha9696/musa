-- 1 запрос
select product, qty from supply
    inner join products p on supply.product_id = p.id
where warehouse_id = 1
and date(supply_date) between '2023-11-01' and '2023-11-03';

-- 2 запрос
select product, qty from debit
    inner join products p on p.id = debit.product_id
where warehouse_id = 1
and date(supply_date) between '2023-11-02' and '2023-11-04';

-- 3 запрос
select category, sum(qty) from supply
    inner join products p on p.id = supply.product_id
    inner join categories c on c.id = p.category_id
where warehouse_id = 1
and date(supply_date) between '2023-11-01' and '2023-11-04'
group by category;

-- 4 запрос
select brand, sum(qty) from supply
    inner join products p on p.id = supply.product_id
    inner join brands b on b.id = p.brand_id
where warehouse_id = 1
and date(supply_date) between '2023-11-01' and '2023-11-04'
group by brand;

-- 5 запрос
select product, qty from availability
    inner join products p on p.id = availability.product_id
where date(exist_date) = '2023-11-04'
order by product;

-- 6 запрос
select product, sum(qty) from supply
    inner join products p on p.id = supply.product_id
where supplier_id = 1
and date(supply_date) between '2023-11-01' and '2023-11-05'
group by product;

-- 7 запрос
select product, sum(qty) from supply
    inner join products p on p.id = supply.product_id
where supplier_id = 1
and warehouse_id = 1
and date(supply_date) between '2023-11-01' and '2023-11-05'
group by product;

-- 8 запрос
select product, sum(qty) from debit
    inner join products p on p.id = debit.product_id
where supplier_id = 1
and warehouse_id = 1
and date(supply_date) between '2023-11-01' and '2023-11-05'
group by product;

-- 9 запрос
select supplier, sum(qty) from supply
    inner join products p on p.id = supply.product_id
    inner join suppliers s on s.id = supply.supplier_id
where product_id = 3
and date(supply_date) between '2023-11-01' and '2023-11-06'
group by supplier
order by sum(qty) desc;

-- 10 запрос
select supplier, sum(qty) from debit
    inner join products p on p.id = debit.product_id
    inner join suppliers s on s.id = debit.supplier_id
where product_id = 2
and date(supply_date) between '2023-11-01' and '2023-11-06'
group by supplier
order by sum(qty) desc;

-- 11 запрос
select product, sum(qty) from movements
    inner join products p on p.id = movements.product_id
where to_warehouse_id = 3
and date(movement_date) between '2023-11-07' and '2023-11-09'
group by product;

-- 12 запрос
select product, sum(qty) from movements
    inner join products p on p.id = movements.product_id
where from_warehouse_id = 4
and date(movement_date) between '2023-11-07' and '2023-11-12'
group by product;