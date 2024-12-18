from django.shortcuts import render
import os

def index(request):
    """
    Display a list of available stock visualizations.
    """
    stock_list = [
        "Tesla_Price",
        "Apple_Price",
        "Google_Price",
        "Microsoft_Price",
        "Ethereum_Price",
        "Nvidia_Price",
        "Meta_Price",
        "Amazon_Price",
        "Gold_Price",
    ]
    return render(request, 'stock/index.html', {'stock_list': stock_list})

def dataset_explore(request):
    return render(request, 'stock/dataset_exp.html')

# View for the home page
def home_view(request):
    return render(request, 'stock/home.html')

# View for the dashboard page
def dashboard_view(request):
    return render(request, 'stock/dashboard.html')

# View for the risk page
def risk_view(request):
    return render(request, 'stock/risk.html')


def visualize_stock(request, stock_name):
    """
    Display the visualization of the selected stock.
    """
    # File path to the visualization
    file_path = os.path.join('static/images', f'{stock_name}_predictions.jpg')

    # Check if the file exists
    if os.path.exists(file_path):
        context = {'stock_name': stock_name, 'file_path': file_path}
    else:
        context = {'stock_name': stock_name, 'error': 'Visualization not found.'}

    return render(request, 'stock/visualize_stock.html', context)
