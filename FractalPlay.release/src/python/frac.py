'''
Fractal code using Python and a Duck.AI query
Reference (retried 2025-07-18):
   https://thelinuxcode.com/plotly-express-scatter-3d/
   https://www.tutorialspoint.com/plotly/plotly_3d_scatter_and_surface_plot.htm
   https://sqlpey.com/python/top-8-methods-to-solve-pandas-append-deprecation-issue/
Non-Primary references
   https://thelinuxcode.com/plotly-express-scatter-3d/ 
   https://www.slingacademy.com/article/pandas-how-to-append-new-rows-to-a-dataframe/ 
   https://medium.com/@devaangnadkarni01/how-to-build-interactive-3d-plots-in-python-d010bb265c2a 
   https://plotly.com/python/3d-camera-controls/ 
Duck.AI query for fractal computation stored in "doc" folder as a URL won't work.
If above URL's are not available in the future,  try browsing them using the "Internet Wayback
Machine" at https://archive.org.
'''


import pandas as pd
import plotly.express as px


def lorenz_attractor(sigma, beta, rho, dt, steps):
    '''
    The Lorenz Attractor Block
    '''
    df = pd.DataFrame( columns=['X', 'Y', 'Z'] )
    loop_iteration = 1
    x, y, z       = 1.0, 1.0, 1.0  # Initial conditions

    for _ in range(steps):
        dx = sigma * (y - x) * dt
        dy = (x * (rho - z) - y) * dt
        dz = (x * y - beta * z) * dt
        x += dx
        y += dy
        z += dz
        print(loop_iteration, x, y, z)
        # use of _append a deprecated (oh well...). Note that with this line you could also get the
        # warning message "FutureWarning: The behavior of DataFrame concatenation with empty or
        # all-NA entries is deprecated. In a future version, this will no longer exclude empty or
        # all-NA columns when determining the result dtypes. To retain the old behavior, exclude the
        # relevant entries before the concat operation."  This line of code commented but left in
        # place as a message to the future.
        #df =df._append( {'X': x, 'Y': y, 'Z': z}, ignore_index=True )
        df.loc[ len(df) ]  =  {'X': x, 'Y': y, 'Z': z, 'loopIteration': loop_iteration}
        loop_iteration = loop_iteration + 1
    fig = px.scatter_3d( df, x='X', y='Y', z='Z' )
    fig.show()

def main():
    ''' Main Block!!'''
    # Parameters
    sigma = 10.0
    beta = 8/3
    rho = 28.0
    dt = 0.01
    steps = 1000

    lorenz_attractor(sigma, beta, rho, dt, steps)


if __name__ == '__main__':
    main()
