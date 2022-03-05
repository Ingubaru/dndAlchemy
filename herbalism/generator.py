import random


#-----------------------------------------------------------------------
# DICE Functions
#-----------------------------------------------------------------------
def getDice4():
	return random.randint(1, 4)


def getDice6():
	return random.randint(1, 6)


def getDice100():
	return random.randint(1, 100)


def getTwoDice6():
	return (getDice6() + getDice6())


#-----------------------------------------------------------------------
# Get ingredients from EVERYWHERE
#-----------------------------------------------------------------------
everywhereIngredients = {
	2:  "Корень Мандрагоры;",
	3:  "Ртутный лишайник;",
	4:  "Ртутный лишайник;",
	5:  "Корень дикого Шалфея;",
	6:  "Корень дикого Шалфея;",
	7:  "Кровьтрава;",
	8:  "Лепестки Змееуста;",
	9:  "Лепестки Змееуста;",
	10: "Семена Молочая;",
	11: "Семена Молочая;",
	12: "Корень Мандрагоры;",
}


def getOneIngredientFromEverywhere():
	diceValue = getTwoDice6();
	if diceValue in [2, 3, 4, 10, 11, 12] and getDice100() >= 75:
		return "Элементальная Вода;"
	else:
		return everywhereIngredients[diceValue]


def getIngredientsFromEverywhere():
	numberOfIngredients = getDice4()	
	ingredients = ""
	for i in range(numberOfIngredients):
		ingredients = ingredients + getOneIngredientFromEverywhere()
	return ingredients


#-----------------------------------------------------------------------
# Get ingredients from other place
#-----------------------------------------------------------------------
arcticIngredients = {
	2:  "Серебряный Гибискус;",
	3:  "Порошок морплоти;",
	4:  "Сердце жлезодрева;",
	5:  "Замороженные саженцы;Замороженные саженцы;",
	6:  getOneIngredientFromEverywhere(),
	7:  getOneIngredientFromEverywhere(),
	8:  getOneIngredientFromEverywhere(),
	9:  "Арктический плющ;Арктический плющ;",
	10: "Фенхелейвый шёлк;",
	11: "Дьявольский плющ;",
	12: "Корень пустоты;",
}

coastIngredients = {
	2:  "Водополох;Водополох;",
	3:  "Шляпка мухомора;",
	4:  "Нектар Гиацинта;",
	5:  "Хромовая Слизь;Хромовая Слизь;",
	6:  getOneIngredientFromEverywhere(),
	7:  getOneIngredientFromEverywhere(),
	8:  getOneIngredientFromEverywhere(),
	9:  "Веточка Лаванды;",
	10: "Синий Кривожаб;",
	11: "Зловонная луковица;",
	12: "Ко-Глонд;",
}

underwaterIngredients = {
	2:  "Водополох;Водополох;",
	3:  "",
	4:  "Нектар Гиацинта;",
	5:  "Хромовая Слизь;Хромовая Слизь;",
	6:  getOneIngredientFromEverywhere(),
	7:  getOneIngredientFromEverywhere(),
	8:  getOneIngredientFromEverywhere(),
	9:  "",
	10: "",
	11: "Зловонная луковица;",
	12: "Ко-Глонд;",
}

desertIngredients = {
	2:  "Ко-Глонд;",
	3:  "Корень Стрела;",
	4:  "Сушёеная Эфедра;",
	5:  "Сок кактуса;Сок кактуса;",
	6:  getOneIngredientFromEverywhere(),
	7:  getOneIngredientFromEverywhere(),
	8:  getOneIngredientFromEverywhere(),
	9:  "Цветы Дракуса;Цветы Дракуса;",
	10: "Бобы Сцили;",
	11: "Ягоды Шипоцвета;",
	12: "Корень пустоты;Элементальная Вода;",
}

forestIngredients = {
	2:  "Листья Харрады;",
	3:  "Ягоды паслёна;",
	4:  "Рвоск;",
	5:  "Вердинская крапива;",
	6:  getOneIngredientFromEverywhere(),
	7:  getOneIngredientFromEverywhere(),
	8:  getOneIngredientFromEverywhere(),
	9:  "Корень Стрела;",
	10: "Сердце жлезодрева;",
	11: "Синий Кривожаб;",
	12: "",
}

forestNightIngredients = {
	2:  "Листья Харрады;",
	3:  "Ягоды паслёна;",
	4:  "Рвоск;",
	5:  "Вердинская крапива;",
	6:  getOneIngredientFromEverywhere(),
	7:  getOneIngredientFromEverywhere(),
	8:  getOneIngredientFromEverywhere(),
	9:  "Корень Стрела;",
	10: "Сердце жлезодрева;",
	11: "Синий Кривожаб;",
	12: "Стебли Гифломы;",
}

fieldIngredients = {
	2:  "Листья Харрады;",
	3:  "Цветы Дракуса;",
	4:  "Веточка Лаванды;Веточка Лаванды;",
	5:  "Корень Стрела;",
	6:  getOneIngredientFromEverywhere(),
	7:  getOneIngredientFromEverywhere(),
	8:  getOneIngredientFromEverywhere(),
	9:  "Бобы Сцили;Бобы Сцили;",
	10: "Сок кактуса;",
	11: "Листохвост;",
	12: "Нектар Гиацинта;",
}

hillIngredients = {
	2:  "Дьявольский кроволист;",
	3:  "Ягоды паслёна;",
	4:  "Листохвост;Листохвост;",
	5:  "Веточка Лаванды;",
	6:  getOneIngredientFromEverywhere(),
	7:  getOneIngredientFromEverywhere(),
	8:  getOneIngredientFromEverywhere(),
	9:  "Сердце жлезодрева;",
	10: "Кисть Генгкоу;",
	11: "Каменный вьюн;Каменный вьюн;",
	12: "Листья Харрады;",
}

mountainIngredients = {
	2:  "Дыхание Василиска;",
	3:  "Замороженные саженцы;Замороженные саженцы;",
	4:  "Арктический плющ;",
	5:  "Сушёеная Эфедра;",
	6:  getOneIngredientFromEverywhere(),
	7:  getOneIngredientFromEverywhere(),
	8:  getOneIngredientFromEverywhere(),
	9:  "Цветы Дракуса;",
	10: "Светопыль шляпки;Светопыль шляпки;",
	11: "Каменный вьюн;",
	12: "Изначальный бальзам;",
}

swampIngredients = {
	2:  "Дьявольский кроволист;",
	3:  "Ягоды Шипоцвета;",
	4:  "Рвоск;",
	5:  "Шляпка мухомора;Шляпка мухомора;",
	6:  getOneIngredientFromEverywhere(),
	7:  getOneIngredientFromEverywhere(),
	8:  getOneIngredientFromEverywhere(),
	9:  "Синий Кривожаб;Синий Кривожаб;",
	10: "Зловонная луковица;",
	11: "Водополох;",
	12: "Изначальный бальзам;",
}

swampRainIngredients = {
	2:  "Дьявольский кроволист;",
	3:  "Ягоды Шипоцвета;",
	4:  "Рвоск;",
	5:  "Шляпка мухомора;Шляпка мухомора;",
	6:  getOneIngredientFromEverywhere(),
	7:  getOneIngredientFromEverywhere(),
	8:  getOneIngredientFromEverywhere(),
	9:  "Синий Кривожаб;Синий Кривожаб;",
	10: "Зловонная луковица;",
	11: "Водополох;Водополох;",
	12: "Изначальный бальзам;",
}

undergroundIngredients = {
	2:  "Изначальный бальзам;Изначальный бальзам;",
	3:  "Серебряный Гибискус;",
	4:  "Дьявольский кроволист;",
	5:  "Хромовая Слизь;",
	6:  "Порошок морплоти;Порошок морплоти;",
	7:  "Фенхелейвый шёлк;",
	8:  "Дьявольский плющ;",
	9:  "Кисть Генгкоу;",
	10: "Светопыль шляпки;Светопыль шляпки;",
	11: "Сияющий синтоцвет;",
	12: "Стебли Гифломы;",
}


def getOneIngredientFromSet(ingredientsSet):
	diceValue = getTwoDice6();
	if diceValue in [2, 3, 4, 10, 11, 12] and getDice100() >= 75:
		return "Элементальная Вода;"
	else:
		ingredient = ingredientsSet[diceValue] 
		if ingredient != "":
			return ingredient 
		else:
			return getOneIngredientFromSet(ingredientsSet)


def getIngredientsFromSet(ingredientsSet):
	numberOfIngredients = getDice4()	
	ingredients = ""
	for i in range(numberOfIngredients):
		ingredients = ingredients + getOneIngredientFromSet(ingredientsSet)
	return ingredients


def getIngredients(regionType):
	if   regionType == 0:  ingredients = getIngredientsFromEverywhere()
	elif regionType == 1:  ingredients = getIngredientsFromSet(arcticIngredients)
	elif regionType == 2:  ingredients = getIngredientsFromSet(coastIngredients)
	elif regionType == 3:  ingredients = getIngredientsFromSet(underwaterIngredients)
	elif regionType == 4:  ingredients = getIngredientsFromSet(desertIngredients)
	elif regionType == 5:  ingredients = getIngredientsFromSet(forestIngredients)
	elif regionType == 6:  ingredients = getIngredientsFromSet(forestNightIngredients)
	elif regionType == 7:  ingredients = getIngredientsFromSet(fieldIngredients)
	elif regionType == 8:  ingredients = getIngredientsFromSet(hillIngredients)
	elif regionType == 9:  ingredients = getIngredientsFromSet(mountainIngredients)
	elif regionType == 10: ingredients = getIngredientsFromSet(swampIngredients)
	elif regionType == 11: ingredients = getIngredientsFromSet(swampRainIngredients)
	elif regionType == 12: ingredients = getIngredientsFromSet(undergroundIngredients)
	else: ingredients = getIngredientsFromEverywhere()
	return ingredients.split(';')[:-1]

