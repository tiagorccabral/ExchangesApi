# Generated by Django 2.0.7 on 2018-07-21 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BitcointradeBitcoinAsk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_coin_value', models.FloatField(verbose_name='Valor da moeda do primeiro ask')),
                ('second_coin_value', models.FloatField(verbose_name='Valor da moeda do segundo ask')),
                ('first_amount', models.FloatField(verbose_name='Quantidade de Bitcoins do primeiro ask')),
                ('second_amount', models.FloatField(verbose_name='Quantidade de Bitcoins do segundo ask')),
                ('saved_at', models.DateTimeField(verbose_name='Data e horario de obtencao dos dados')),
            ],
        ),
        migrations.CreateModel(
            name='BitcointradeBitcoinBid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_coin_value', models.FloatField(verbose_name='Valor da moeda do primeiro bid')),
                ('second_coin_value', models.FloatField(verbose_name='Valor da moeda do segundo bid')),
                ('first_amount', models.FloatField(verbose_name='Quantidade de Bitcoins do primeiro bid')),
                ('second_amount', models.FloatField(verbose_name='Quantidade de Bitcoins do segundo bid')),
                ('saved_at', models.DateTimeField(verbose_name='Data e horario de obtencao dos dados')),
            ],
        ),
        migrations.CreateModel(
            name='BitcointradeEthereumsAsk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_coin_value', models.FloatField(verbose_name='Valor da moeda do primeiro ask')),
                ('second_coin_value', models.FloatField(verbose_name='Valor da moeda do segundo ask')),
                ('first_amount', models.FloatField(verbose_name='Quantidade de Ethereums do primeiro ask')),
                ('second_amount', models.FloatField(verbose_name='Quantidade de Ethereums do segundo ask')),
                ('saved_at', models.DateTimeField(verbose_name='Data e horario de obtencao dos dados')),
            ],
        ),
        migrations.CreateModel(
            name='BitcointradeEthereumsBid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_coin_value', models.FloatField(verbose_name='Valor da moeda do primeiro bid')),
                ('second_coin_value', models.FloatField(verbose_name='Valor da moeda do segundo bid')),
                ('first_amount', models.FloatField(verbose_name='Quantidade de Ethereums do primeiro bid')),
                ('second_amount', models.FloatField(verbose_name='Quantidade de Ethereums do segundo bid')),
                ('saved_at', models.DateTimeField(verbose_name='Data e horario de obtencao dos dados')),
            ],
        ),
        migrations.CreateModel(
            name='BitstampBitcoinAsk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_coin_value', models.FloatField(verbose_name='Valor da moeda do primeiro ask')),
                ('second_coin_value', models.FloatField(verbose_name='Valor da moeda do segundo ask')),
                ('first_amount', models.FloatField(verbose_name='Quantidade de Bitcoins do primeiro ask')),
                ('second_amount', models.FloatField(verbose_name='Quantidade de Bitcoins do segundo ask')),
                ('saved_at', models.DateTimeField(verbose_name='Data e horario de obtencao dos dados')),
            ],
        ),
        migrations.CreateModel(
            name='BitstampBitcoinBid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_coin_value', models.FloatField(verbose_name='Valor da moeda do primeiro bid')),
                ('second_coin_value', models.FloatField(verbose_name='Valor da moeda do segundo bid')),
                ('first_amount', models.FloatField(verbose_name='Quantidade de Bitcoins do primeiro bid')),
                ('second_amount', models.FloatField(verbose_name='Quantidade de Bitcoins do segundo bid')),
                ('saved_at', models.DateTimeField(verbose_name='Data e horario de obtencao dos dados')),
            ],
        ),
        migrations.CreateModel(
            name='BitstampEthBtcAsk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_coin_value', models.FloatField(verbose_name='Valor da moeda do primeiro ask')),
                ('first_amount', models.FloatField(verbose_name='Quantidade de moedas do primeiro ask')),
                ('saved_at', models.DateTimeField(verbose_name='Data e horario da obtencao dos dados')),
            ],
        ),
        migrations.CreateModel(
            name='BitstampEthBtcBid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_coin_value', models.FloatField(verbose_name='Valor da moeda do primeiro bid')),
                ('first_amount', models.FloatField(verbose_name='Quantidade de moedas do primeiro bid')),
                ('saved_at', models.DateTimeField(verbose_name='Data e horario da obtencao dos dados')),
            ],
        ),
        migrations.CreateModel(
            name='BitstampEthereumsAsk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_coin_value', models.FloatField(verbose_name='Valor da moeda do primeiro ask')),
                ('second_coin_value', models.FloatField(verbose_name='Valor da moeda do segundo ask')),
                ('first_amount', models.FloatField(verbose_name='Quantidade de Ethereums do primeiro ask')),
                ('second_amount', models.FloatField(verbose_name='Quantidade de Ethereums do segundo ask')),
                ('saved_at', models.DateTimeField(verbose_name='Data e horario de obtencao dos dados')),
            ],
        ),
        migrations.CreateModel(
            name='BitstampEthereumsBid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_coin_value', models.FloatField(verbose_name='Valor da moeda do primeiro bid')),
                ('second_coin_value', models.FloatField(verbose_name='Valor da moeda do segundo bid')),
                ('first_amount', models.FloatField(verbose_name='Quantidade de Ethereums do primeiro bid')),
                ('second_amount', models.FloatField(verbose_name='Quantidade de Ethereums do segundo bid')),
                ('saved_at', models.DateTimeField(verbose_name='Data e horario de obtencao dos dados')),
            ],
        ),
        migrations.CreateModel(
            name='SpreadMaxAsk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spread', models.FloatField(verbose_name='Valor do max spread para asks')),
                ('saved_at', models.DateTimeField(verbose_name='Data e horario da obtencao dos dados')),
            ],
        ),
        migrations.CreateModel(
            name='SpreadMaxBid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spread', models.FloatField(verbose_name='Valor do max spread para bids')),
                ('saved_at', models.DateTimeField(verbose_name='Data e horario da obtencao dos dados')),
            ],
        ),
    ]
