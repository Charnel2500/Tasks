import csv

with open('data.csv') as csvfile:
    readCSV = csv.DictReader(csvfile, delimiter=',')

    for row in readCSV:
        print(row)
    for row in readCSV:
        price * quantity

    with open('top_products.csv', 'w') as new_file:
        fieldnames = ['matching_id','total_price','avg_price,currency', 'ignored_products_count']

        csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter=',')

        csv_writer.writeheader()

        for line in readCSV:
            readCSV.writerow(line['matching_id','total_price','avg_price,currency', 'ignored_products_count'])

with open('currencies.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')

    for row in readCSV:
        print(row)



with open('matchings.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')

    for row in readCSV:
        print(row)