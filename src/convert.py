import tensorflow as tf

graph_def_file = "../model/output_graph.pb"
input_arrays = ["Placeholder"]
output_arrays = ["CTCGreedyDecoder"]


converter = tf.lite.TFLiteConverter.from_frozen_graph(graph_def_file, input_arrays, output_arrays)
tflite_model = converter.convert()
open("converted_model.tflite", "wb").write(tflite_model)
