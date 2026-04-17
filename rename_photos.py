import os
import shutil

# 定义中英文映射字典
rename_map = {
    "“合影”.jpg": "group_photo.jpg",
    "一舞寄相思.jpg": "dance_for_you.jpg",
    "一起听.jpg": "listening_together.jpg",
    "一起摇太阳.jpg": "shake_the_sun_together.jpg",
    "上台前.jpg": "before_stage.jpg",
    "五月.jpg": "may.jpg",
    "信.jpg": "letter.jpg",
    "冬.jpg": "winter.jpg",
    "卡哇伊的笑.jpg": "kawaii_smile.jpg",
    "卡门！.jpg": "carmen.jpg",
    "双人成行.jpg": "it_takes_two.jpg",
    "四月的油菜花海.jpg": "april_canola_flower_sea.jpg",
    "回眸.jpg": "looking_back.jpg",
    "夏.jpg": "summer.jpg",
    "夜色之海.jpg": "night_sea.jpg",
    "宁静的午后.jpg": "peaceful_afternoon.jpg",
    "定情礼物.jpg": "love_token.jpg",
    "寻野.jpg": "seeking_wild.jpg",
    "小火车.jpg": "little_train.jpg",
    "旧城故事.jpg": "old_city_story.jpg",
    "明媚烈焰！.jpg": "bright_flame.jpg",
    "春.jpg": "spring.jpg",
    "晴天.jpg": "sunny_day.jpg",
    "樱花下落的速度.jpg": "speed_of_falling_cherry_blossoms.jpg",
    "毕业同框.jpg": "graduation_frame.jpg",
    "浮生若梦.jpg": "life_is_like_a_dream.jpg",
    "海的那边.jpg": "over_the_sea.jpg",
    "清凉的溪.jpg": "cool_stream.jpg",
    "游园.jpg": "garden_tour.jpg",
    "猫咖.jpg": "cat_cafe.jpg",
    "玄武湖泛舟.jpg": "boating_on_xuanwu_lake.jpg",
    "玫瑰.jpg": "rose.jpg",
    "看我干嘛.jpg": "why_looking_at_me.jpg",
    "碧空之下.jpg": "under_the_blue_sky.jpg",
    "祈缘99.jpg": "praying_for_destiny_99.jpg",
    "秋.jpg": "autumn.jpg",
    "穿越森林.jpg": "through_the_forest.jpg",
    "簪花.jpg": "hairpin_flower.jpg",
    "糖水.jpg": "sweet_soup.jpg",
    "红叶最多情.jpg": "red_leaves_most_affectionate.jpg",
    "纪念日.jpg": "anniversary.jpg",
    "绿意之中.jpg": "in_the_greenery.jpg",
    "美味蟹黄面.jpg": "delicious_crab_roe_noodles.jpg",
    "草地.jpg": "grassland.jpg",
    "落日下.jpg": "under_the_sunset.jpg",
    "蓝色爱恋.jpg": "blue_love.jpg",
    "蝉鸣的夏.jpg": "cicada_chirping_summer.jpg",
    "起风了.jpg": "the_wind_rises.jpg",
    "雪.jpg": "snow.jpg"
}

photo_dir = r"d:\Desktop\纪念日网站\2005425\照片"

for cn_name, en_name in rename_map.items():
    old_path = os.path.join(photo_dir, cn_name)
    new_path = os.path.join(photo_dir, en_name)
    if os.path.exists(old_path):
        os.rename(old_path, new_path)
        print(f"Renamed {cn_name} to {en_name}")
    else:
        print(f"File not found: {cn_name}")
