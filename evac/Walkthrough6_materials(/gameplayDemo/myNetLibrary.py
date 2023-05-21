import numpy as np

class MLP_NeuralNetwork(object):
    def __init__(self, numInput, numHidden, numOutput):
        self.fitness = 0
        self.numInput = numInput + 1
        self.numHidden = numHidden + 1
        self.numOutput = numOutput

        self.wi = np.random.randn(self.numInput, self.numHidden) 
        self.wo = np.random.randn(self.numHidden, self.numOutput)

        self.ReLU = lambda x : max(0,x)

    def feedForward(self, inputs):
        h1 = self.ReLU(np.dot(self.wi, inputs))  # hidden layer
        out = self.ReLU(np.dot(self.wo, h1))     # output layer
        return out

    def getOutput(self):
        return self.ao[:]

    def getWeightsLinear(self):
        Wgenome = []
        for i in range(self.numInput):
            for j in range(self.numHidden - 1): # don't want to feed in to bias node
                Wgenome.append(self.wi[i][j])

        for k in range(self.numOutput):
            for j in range(self.numHidden):
                Wgenome.append(self.wo[j][k])
        return Wgenome

    def getWeightsInputToHidden(self):
        Wgenome = []
        for i in range(self.numInput):
            for j in range(self.numHidden - 1):
                Wgenome.append(self.wi[i][j])

        return Wgenome

    def getWeightsHiddenToOutput(self):
        Wgenome = []
        for k in range(self.numOutput):
            for j in range(self.numHidden):
                Wgenome.append(self.wo[j][k])
        return Wgenome
        
    # Set weights from a linear representation
    def setWeightsLinear(self, Wgenome):
        #Wgenome = self.getWeights()
        WgenomeIndex = 0
        for i in range(self.numInput):
            for j in range(self.numHidden - 1):
                self.wi[i][j] = Wgenome[WgenomeIndex]
                WgenomeIndex += 1

        for k in range(self.numOutput):
            for j in range(self.numHidden):
                self.wo[j][k] = Wgenome[WgenomeIndex]
                WgenomeIndex += 1
        return Wgenome
