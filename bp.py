def gen_image(prompt):
  client = Client("https://nota-ai-compressed-stable-diffusion.hf.space/")
  result = client.predict(
				prompt,	# str  in 'Input Prompt' Textbox component
				" ",	# str  in 'Negative Prompt' Textbox component
				4,	# int | float (numeric value between 4 and 11) in 'Guidance Scale' Slider component
				10,	# int | float (numeric value between 10 and 75) in 'Denoising Steps' Slider component
				0,	# int | float (numeric value between 0 and 999999) in 'Random Seed' Slider component
				fn_index=1
  )
  img_p=result[0]
  return img_p
