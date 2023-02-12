from rest_framework import serializers

from .models import AdvertisingBanner, NoticeBanner, PartialData


class NoticeBannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = NoticeBanner
        fields = (
            "header_banner",
            "header_banner_mobile",
            "header_banner_url",
            "first_row_first",
            "first_row_first_url",
            "first_row_second",
            "first_row_second_url",
            "second_row_first",
            "second_row_first_url",
            "second_row_second",
            "second_row_second_url",
        )

    # def to_representation(self, instance):
    # for data in self.fields:

    #     data = {}
    #     print(dir(instance))
    #     for item in self.fields:
    #         keyword_name = str(item.split('_')[0])
    #         print(ke)
    #         for obj in filter(lambda x: x.find(keyword_name), dir(instance)):
    #             data[obj] = {
    #                 'image': 'media/' + instance.__dict__.get(item),
    #                 'url': instance.__dict__.get(instance.__dict__.get(item) + '_url')
    #             }
    #
    # return data


# def to_representation(self, instance):
#     data = {}
#     header = {}
#     first_row = {}
#     second_row = {}
#     for item in self.fields:
#         if item.startswith('header'):
#             if item.find('url'):
#                 first_row[item] = instance.__dict__.get(item)
#                 continue
#             else:
#                 first_row[item] = 'media/' + instance.__dict__.get(item)
#                 continue
#         elif item.startswith('first'):
#             if item.find('url'):
#                 first_row[item] = instance.__dict__.get(item)
#                 continue
#             else:
#                 first_row[item] = 'media/' + instance.__dict__.get(item)
#                 continue
#         else:
#             if item.find('url'):
#                 first_row[item] = instance.__dict__.get(item)
#                 continue
#             else:
#                 first_row[item] = 'media/' + instance.__dict__.get(item)
#         data["header"] = header
#         data["first_row"] = first_row
#         data["second_row"] = second_row
#     return data


class AdvertisingBannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdvertisingBanner
        fields = (
            "first_row_first_image",
            "first_row_second_image",
            "first_row_third_image",
            "first_row_fourth_image",
            "second_row_first_image",
            "second_row_second_image",
            "second_row_third_image",
            "second_row_fourth_image",
            "third_row_first_image",
            "third_row_second_image",
            "third_row_third_image",
            "third_row_fourth_image",
        )

    def to_representation(self, instance):
        data = {}
        for item in self.fields:
            keyword_name = str(item[:-6])
            data[keyword_name] = {
                "image": "media/" + instance.__dict__.get(item),
                "url": instance.__dict__.get(keyword_name + "_url"),
            }
        return data


class PartialDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartialData
        fields = (
            "special_suggestion_text",
            "special_suggestion_image",
            "best_seller_text",
            "best_seller_image",
            "product_text",
            "product_image",
            "mid_banner_text",
            "mid_banner_image",
        )
