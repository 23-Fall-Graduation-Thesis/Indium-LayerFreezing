import torch
import torchvision
import torchvision.transforms as transforms
from torch.utils.data import DataLoader, random_split
from dataset_dir.cub200 import Cub2011

def datasetload(dataset_name, shuffle=True):
    if dataset_name == 'cifar10':
        return Cifar10(shuffle)
    elif dataset_name == 'cifar100':
        return Cifar100(shuffle)
    elif dataset_name == 'svhn':
        return SVHN(shuffle)
    elif dataset_name == 'cub':
        return CUB200(shuffle)



def Cifar10(shuffle):
    n_class = 10

    transform = transforms.Compose([
        transforms.Resize(224),
        transforms.ToTensor(), 
        transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
    ])
    
    batch_size = 64
    
    train_dataset = torchvision.datasets.CIFAR10(root='./data/cifar10', train=True, 
                                            download=True, transform=transform)
    dataset_size = len(train_dataset)
    train_size = int(dataset_size * 0.8)
    valid_size = dataset_size - train_size
    trainset, validset = random_split(train_dataset, [train_size, valid_size])
    
    trainloader = DataLoader(trainset, batch_size, shuffle=shuffle, drop_last=True, num_workers=2)
    validloader = DataLoader(validset, batch_size, shuffle=shuffle, drop_last=True, num_workers=2)
    
    testset = torchvision.datasets.CIFAR10(root='./data/cifar10', train=False, download=True, transform=transform)
    testloader = DataLoader(testset, batch_size, shuffle=shuffle, drop_last=True, num_workers=2)
    
    # classes = {'plane', 'car', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck'}
    
    return trainloader, validloader, testloader, n_class

def Cifar100(shuffle):
    n_class = 100

    transform = transforms.Compose([
        transforms.Resize(224),
        transforms.ToTensor(),
        transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
    ])
    
    batch_size = 64
    
    train_dataset = torchvision.datasets.CIFAR100(root='./data/cifar100', train=True, 
                                                  download=True, transform=transform)
    dataset_size = len(train_dataset)
    train_size = int(dataset_size * 0.8)
    valid_size = dataset_size - train_size
    trainset, validset = random_split(train_dataset, [train_size, valid_size])
    
    trainloader = DataLoader(trainset, batch_size, shuffle=shuffle, drop_last=True, num_workers=2)
    validloader = DataLoader(validset, batch_size, shuffle=shuffle, drop_last=True, num_workers=2)
    
    testset = torchvision.datasets.CIFAR100(root='./data/cifar100', train=False, download=True, transform=transform)
    testloader = DataLoader(testset, batch_size, shuffle=shuffle, drop_last=True, num_workers=2)
    
    return trainloader, validloader, testloader, n_class
    

def SVHN(shuffle):
    n_class = 10
    
    transform = transforms.Compose([
        transforms.Resize(224),
        transforms.ToTensor(), 
        transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
    ])
    
    batch_size = 64
    
    svhn = torchvision.datasets.SVHN(root='./data/svhn', transform=transform, download=True)
    train_indices = torch.arange(0, 50000)
    valid_indices = torch.arange(50000, 60000)
    test_indices = torch.arange(60000, 70000)
    train_svhn = torch.utils.data.Subset(svhn, train_indices)
    valid_svhn = torch.utils.data.Subset(svhn, valid_indices)
    test_svhn = torch.utils.data.Subset(svhn, test_indices)
    
    trainloader = DataLoader(train_svhn, batch_size, shuffle=shuffle, drop_last=True, num_workers=2)
    validloader = DataLoader(valid_svhn, batch_size, shuffle=shuffle, drop_last=True, num_workers=2)
    testloader = DataLoader(test_svhn, batch_size, shuffle=shuffle, drop_last=True, num_workers=2)
    
    return trainloader, validloader, testloader, n_class

def CUB200(shuffle):
    n_class = 200

    transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(), 
        transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
    ])
    
    batch_size = 64
    
    train_dataset = Cub2011(root='./data/cub-200-2011', transform=transform, download=True, train=True)
    dataset_size = len(train_dataset)
    train_size = int(dataset_size * 0.8)
    valid_size = dataset_size - train_size
    trainset, validset = random_split(train_dataset, [train_size, valid_size])
    
    trainloader = DataLoader(trainset, batch_size, shuffle=shuffle, drop_last=True, num_workers=2)
    validloader = DataLoader(validset, batch_size, shuffle=shuffle, drop_last=True, num_workers=2)
    
    test_dataset = Cub2011(root='./data/cub-200-2011', transform=transform, download=True, train=False)
    testloader = DataLoader(test_dataset, batch_size, shuffle=shuffle, drop_last=True, num_workers=2)
    
    return trainloader, validloader, testloader, n_class