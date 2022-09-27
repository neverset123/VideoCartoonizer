import paddlehub as hub

module = hub.Module(name="ernie_vilg")
text_prompts = ["哆啦A梦见到了小黄人，家里"]
styles = ['油画','水彩','粉笔画','卡通','儿童画','蜡笔画','探索无限']
images = module.generate_image(text_prompts=text_prompts, style=styles[0],  output_dir='./ernie_vilg_out/')  