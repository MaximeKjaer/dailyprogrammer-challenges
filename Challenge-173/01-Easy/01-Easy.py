conversion = raw_input('What would you like to convert? ').lower()

typo_corrections = {
	'metres': 'metres', 'metre': 'metres', 'meter': 'metres', 'meters': 'metres', 'm': 'metres',
	'inches': 'inches', 'inch': 'inches', 'in': 'inches',
	'miles': 'miles', 'mile': 'miles', 'mi': 'miles',
	'attoparsecs': 'attoparsecs', 'attoparsec': 'attoparsecs', 'apc': 'attoparsecs',
	'kilograms': 'kilograms', 'kilogram': 'kilograms', 'kg': 'kilograms',
	'pounds': 'pounds', 'pound': 'pounds', 'lb': 'pounds', 'lbs': 'pounds',
	'ounces': 'ounces', 'ounce': 'ounces', 'oz': 'ounces',
	'hogsheads of beryllium': 'hogsheads of beryllium', 'hhd of beryllium': 'hogsheads of beryllium','hob': 'hogsheads of beryllium'
}

unit_metadata = {
	'metres': {'type': 'length', 'value': 1}, # m will be the standard unit (as per )
	'inches': {'type': 'length', 'value': 0.0254},
	'miles':  {'type': 'length', 'value': 1609.34},
	'attoparsecs': {'type': 'length', 'value': 0.030856},
	'kilograms': {'type': 'mass', 'value': 1}, # kg will be the standard unit
	'pounds': {'type': 'mass', 'value': 0.453592},
	'ounces': {'type': 'mass', 'value': 0.0283495},
	'hogsheads of beryllium': {'type': 'mass', 'value': 440.7}
}

def converter(text):
	text = text.replace('  ', ' ').split(' ')
	amount = int(text[0])
	unit_a = typo_corrections[text[1]]
	unit_b = typo_corrections[text[3]]
	if unit_metadata[unit_a]['type']==unit_metadata[unit_b]['type']:
		converted = (amount*unit_metadata[unit_a]['value'])/unit_metadata[unit_b]['value']
		print amount, unit_a, 'is', converted, unit_b
	else:
		print amount, unit_a, 'can\'t be converted to', unit_b


converter(conversion)
