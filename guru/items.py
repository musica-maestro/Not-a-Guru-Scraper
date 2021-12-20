import scrapy
from scrapy.item import Item, Field
from itemloaders.processors import MapCompose, TakeFirst

def country_parser(text):
    try:
        return text.split()[-1]
    except:
        return ''

class GuruItem(scrapy.Item):
    name  = Field(
        input_processor = MapCompose(str.strip),
        output_processor = TakeFirst()
    )
    website  = Field(
        input_processor = MapCompose(str.strip),
        output_processor = TakeFirst()
    )
    rating  = Field(
        input_processor = MapCompose(str.strip),
        output_processor = TakeFirst()
    )
    country  = Field(
        input_processor = MapCompose(str.strip),
        output_processor = TakeFirst()
    )
    number_of_employers  = Field(
        input_processor = MapCompose(str.strip),
        output_processor = TakeFirst()
    )
    member_since  = Field(
        input_processor = MapCompose(str.strip),
        output_processor = TakeFirst()
    )
    description  = Field(
        input_processor = MapCompose(str.strip),
        output_processor = TakeFirst()
    )
    guru_skills  = Field(
        input_processor = MapCompose(str.strip),
        output_processor = TakeFirst()
    )
    guru_services  = Field(
        input_processor = MapCompose(str.strip),
        output_processor = TakeFirst()
    )
    guru_avg_price_per_hour  = Field(
        input_processor = MapCompose(str.strip),
        output_processor = TakeFirst()
    )
