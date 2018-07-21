from django.db import models


# Data from Bitcointrade and Bitstamp about Bitcoins


class BitcointradeBitcoinBid(models.Model):

    first_coin_value = models.FloatField('Valor da moeda do primeiro bid')
    second_coin_value = models.FloatField('Valor da moeda do segundo bid')
    first_amount = models.FloatField('Quantidade de Bitcoins do primeiro bid')
    second_amount = models.FloatField('Quantidade de Bitcoins do segundo bid')

    saved_at = models.DateTimeField('Data e horario de obtencao dos dados')


class BitcointradeBitcoinAsk(models.Model):

    first_coin_value = models.FloatField('Valor da moeda do primeiro ask')
    second_coin_value = models.FloatField('Valor da moeda do segundo ask')
    first_amount = models.FloatField('Quantidade de Bitcoins do primeiro ask')
    second_amount = models.FloatField('Quantidade de Bitcoins do segundo ask')

    saved_at = models.DateTimeField('Data e horario de obtencao dos dados')


class BitstampBitcoinBid(models.Model):

    first_coin_value = models.FloatField('Valor da moeda do primeiro bid')
    second_coin_value = models.FloatField('Valor da moeda do segundo bid')
    first_amount = models.FloatField('Quantidade de Bitcoins do primeiro bid')
    second_amount = models.FloatField('Quantidade de Bitcoins do segundo bid')

    saved_at = models.DateTimeField('Data e horario de obtencao dos dados')


class BitstampBitcoinAsk(models.Model):

    first_coin_value = models.FloatField('Valor da moeda do primeiro ask')
    second_coin_value = models.FloatField('Valor da moeda do segundo ask')
    first_amount = models.FloatField('Quantidade de Bitcoins do primeiro ask')
    second_amount = models.FloatField('Quantidade de Bitcoins do segundo ask')

    saved_at = models.DateTimeField('Data e horario de obtencao dos dados')

# Data from Bitcointrade and Bitstamp about Ethereum


class BitcointradeEthereumsBid(models.Model):

    first_coin_value = models.FloatField('Valor da moeda do primeiro bid')
    second_coin_value = models.FloatField('Valor da moeda do segundo bid')
    first_amount = models.FloatField('Quantidade de Ethereums do primeiro bid')
    second_amount = models.FloatField('Quantidade de Ethereums do segundo bid')

    saved_at = models.DateTimeField('Data e horario de obtencao dos dados')


class BitcointradeEthereumsAsk(models.Model):

    first_coin_value = models.FloatField('Valor da moeda do primeiro ask')
    second_coin_value = models.FloatField('Valor da moeda do segundo ask')
    first_amount = models.FloatField('Quantidade de Ethereums do primeiro ask')
    second_amount = models.FloatField('Quantidade de Ethereums do segundo ask')

    saved_at = models.DateTimeField('Data e horario de obtencao dos dados')


class BitstampEthereumsBid(models.Model):

    first_coin_value = models.FloatField('Valor da moeda do primeiro bid')
    second_coin_value = models.FloatField('Valor da moeda do segundo bid')
    first_amount = models.FloatField('Quantidade de Ethereums do primeiro bid')
    second_amount = models.FloatField('Quantidade de Ethereums do segundo bid')

    saved_at = models.DateTimeField('Data e horario de obtencao dos dados')


class BitstampEthereumsAsk(models.Model):

    first_coin_value = models.FloatField('Valor da moeda do primeiro ask')
    second_coin_value = models.FloatField('Valor da moeda do segundo ask')
    first_amount = models.FloatField('Quantidade de Ethereums do primeiro ask')
    second_amount = models.FloatField('Quantidade de Ethereums do segundo ask')

    saved_at = models.DateTimeField('Data e horario de obtencao dos dados')


class BitstampEthBtcBid(models.Model):

    first_coin_value = models.FloatField('Valor da moeda do primeiro bid')
    first_amount = models.FloatField('Quantidade de moedas do primeiro bid')

    saved_at = models.DateTimeField('Data e horario da obtencao dos dados')


class BitstampEthBtcAsk(models.Model):
    first_coin_value = models.FloatField('Valor da moeda do primeiro ask')
    first_amount = models.FloatField('Quantidade de moedas do primeiro ask')

    saved_at = models.DateTimeField('Data e horario da obtencao dos dados')


class SpreadMaxAsk(models.Model):

    spread = models.FloatField('Valor do max spread para asks')

    saved_at = models.DateTimeField('Data e horario da obtencao dos dados')


class SpreadMaxBid(models.Model):

    spread = models.FloatField('Valor do max spread para bids')

    saved_at = models.DateTimeField('Data e horario da obtencao dos dados')
