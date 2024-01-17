# Quickstart

## Setup the model
We basically start getting the training and test data from **FashionMNIST** which is one of the many available vision datasets for pytorch.
```bash
(dev) ~z➤ python 01.py
Shape of X [N, C, H, W]: torch.Size([64, 1, 28, 28])
Shape of y: torch.Size([64]) torch.int64
```

Then we create the model.
Here we basically we use a lot `nn.Module` lib, it helps creating the NeuralNetwork and other parameters for itself. We are also using `cuda` (bcoz I have NVIDIA like the pros :skull:) where the model will be processed.
(dev) ~z➤ python 01.py
```bash
Shape of X [N, C, H, W]: torch.Size([64, 1, 28, 28])
Shape of y: torch.Size([64]) torch.int64
(dev) ~z➤ python 01.py
Using cuda device
NeuralNetwork(
  (flatten): Flatten(start_dim=1, end_dim=-1)
  (linear_relu_stack): Sequential(
    (0): Linear(in_features=784, out_features=512, bias=True)
    (1): ReLU()
    (2): Linear(in_features=512, out_features=512, bias=True)
    (3): ReLU()
    (4): Linear(in_features=512, out_features=10, bias=True)
  )
)
```

## Train and Test
With use of Loss Function and Optimizer we can train the model so it can make predictions and propagate results back in order to tune better the model's params.
We should also **test** the model to evaluate wether its learning or not.

The loss function gets the info on how well the model performed and the optimizer tunes the model to make it better the next time.

After training and testing the model during various epochs:
```bash
...
loss: 0.833402  [57664/60000]
Test Error:
 Accuracy: 70.0%, Avg loss: 0.819294

Epoch 10
-------------------------------
loss: 0.833612  [   64/60000]
loss: 0.903723  [ 6464/60000]
loss: 0.679648  [12864/60000]
loss: 0.873493  [19264/60000]
loss: 0.766314  [25664/60000]
loss: 0.765345  [32064/60000]
loss: 0.839947  [38464/60000]
loss: 0.817787  [44864/60000]
loss: 0.811614  [51264/60000]
loss: 0.804626  [57664/60000]
Test Error:
 Accuracy: 71.2%, Avg loss: 0.787830

```

## Saving, Loading and Testing the model
After training and validating the model, we can now save and load and manually test the model.
```bash
Done!
Predicted: "Ankle boot", Actual: "Ankle boot"
```

Check all of this examples in the file: :link: [labs/01.py](labs/01.py)
