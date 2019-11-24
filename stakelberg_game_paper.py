#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np

class Customer():	# Utility function of customer: U_i = X_i*d_i - alpha_i*(d_i^2)/2 - p*d_i
	def __init__(self, X, alpha):
		self.X = X
		self.alpha = alpha

customer_array = []

def intialize_customer_array():
	customer_array.append(Customer(1,2.5))
	customer_array.append(Customer(1,2.5))
	customer_array.append(Customer(2,2.5))
	customer_array.append(Customer(2,2.5))
	customer_array.append(Customer(2,2.5))
	customer_array.append(Customer(3,2.5))
	customer_array.append(Customer(3,2.5))
	customer_array.append(Customer(3,2.5))
	customer_array.append(Customer(4,2.5))
	customer_array.append(Customer(4,2.5))

def calculate_F_and_G():
	global F, G
	F = 0
	G = 0
	for i in range(len(customer_array)):
		F = F + customer_array[i].X / customer_array[i].alpha
		G = G + 1 / customer_array[i].alpha
	print("F = " + str(F))
	print("G = " + str(G))

def calculate_E_m_from_C_g_and_C_m(C_g, C_m):
	a = -16
	b = (F/2/G - C_m) * 24 * G
	c = 0
	d = (G*C_g - F)**3
	coefs = [a, b, c, d]
	roots = np.roots(coefs)
	return min(max(roots), F/2)

def plot_E_m_vary_C_m_keeping_C_m_constant():
	x_plot = []
	y_plot = []

	for C_g in [0.5, 0.7, 1.0]:
		for C_m in np.arange(0, 0.7+0.05, 0.05):
			if C_m >= C_g/2:
				E_m_star = 0				
			else:
				E_m_star = calculate_E_m_from_C_g_and_C_m(C_g, C_m)
			x_plot.append(C_m)
			y_plot.append(E_m_star)

	l  = int(len(x_plot)/3)

	plt.figure(1)
	plt.plot(x_plot[0:l], y_plot[0:l], label = r'$C_g$' + '= 0.5', marker = '^', fillstyle = 'none')
	plt.plot(x_plot[l:2*l], y_plot[l:2*l], label = r'$C_g$' + '= 0.7', marker = 'o', fillstyle = 'none')
	plt.plot(x_plot[2*l:3*l], y_plot[2*l:3*l], label = r'$C_g$' + '= 1.0', marker = 's', fillstyle = 'none')
	plt.legend()
	plt.xlabel('Price of electricity from Option I, ' + r'$C_m$')
	plt.ylabel('Optimal Amount to procure from Source 1 ('+ r'$E_m^*$)')
	plt.grid(True)
	plt.savefig('figure3.png')

def plot_E_g_vary_beta_keeping_C_g_C_m_constant():
	x_plot = []
	y_plot = []
	C_g_C_m_array = [[0.5, 0.24], [0.5, 0.1], [1.0, 0.1]]

	for array in C_g_C_m_array:
		C_g = array[0]
		C_m = array[1]
		E_m = calculate_E_m_from_C_g_and_C_m(C_g, C_m)
		for beta in np.arange(0, 1+0.05, 0.05):
			if E_m*beta < (F - G*C_g)/2:
				E_g_star = (F - G*C_g - 2*E_m*beta)/2
			else:
				E_g_star = 0
			x_plot.append(beta)
			y_plot.append(E_g_star)

	l  = int(len(x_plot)/3)

	plt.figure(2)
	plt.plot(x_plot[0:l], y_plot[0:l], label = '(' + r'$C_g$,$C_m$) = (0.5, 0.24)', marker = '^', fillstyle = 'none')
	plt.plot(x_plot[l:2*l], y_plot[l:2*l], label = '(' + r'$C_g$,$C_m$) = (0.5, 0.1)', marker = 'o', fillstyle = 'none')
	plt.plot(x_plot[2*l:3*l], y_plot[2*l:3*l], label = '(' + r'$C_g$,$C_m$) = (1.0, 0.1)', marker = 's', fillstyle = 'none')
	plt.legend()
	plt.xlabel('Realization Factor (' + r'$\beta$)')
	plt.ylabel('Optimal Amount to procure from Source 2 ('+ r'$E_g^*$)')
	plt.grid(True)
	plt.savefig('figure4.png')

def plot_p_vary_beta_keeping_C_g_C_m_constant():
	x_plot = []
	y_plot = []
	C_g_C_m_array = [[0.5, 0.24], [0.5, 0.1], [1.0, 0.1]]

	for array in C_g_C_m_array:
		C_g = array[0]
		C_m = array[1]
		p_star = 0
		E_lm_star = calculate_E_m_from_C_g_and_C_m(C_g, C_m)
		for beta in np.arange(0, 1+0.05, 0.05):
			if beta <= (F-G*C_g)/2/E_lm_star:
				p_star = (F+G*C_g)/2/G
			else:
				p_star = (F-beta*E_lm_star)/G

			x_plot.append(beta)
			y_plot.append(p_star)

	l  = int(len(x_plot)/3)

	plt.figure(3)
	plt.plot(x_plot[0:l], y_plot[0:l], label = '(' + r'$C_g$,$C_m$) = (0.5, 0.24)', marker = '^', fillstyle = 'none')
	plt.plot(x_plot[l:2*l], y_plot[l:2*l], label = '(' + r'$C_g$,$C_m$) = (0.5, 0.1)', marker = 'o', fillstyle = 'none')
	plt.plot(x_plot[2*l:3*l], y_plot[2*l:3*l], label = '(' + r'$C_g$,$C_m$) = (1.0, 0.1)', marker = 's', fillstyle = 'none')
	plt.legend()
	plt.xlabel('Realization Factor (' + r'$\beta$)')
	plt.ylabel('Optimal Price ('+ r'$p^*$)')
	plt.ylim([0,2])
	plt.grid(True)
	plt.savefig('figure5.png')
		
def plot_profit_vary_C_m_keeping_C_g_constant():
	x_plot = []
	y_plot_1 = []
	y_plot_2 = []
	C_g = 2

	for C_m in np.arange(0.2, C_g/2+0.05, 0.05):
		E_lm_star = calculate_E_m_from_C_g_and_C_m(C_g, C_m)
		R_l_1 = (F - G*C_g)**3/24/G/E_lm_star+(F/2/G-C_m)*E_lm_star-E_lm_star**2/3/G
		R_h = F**2/4/G+G*C_g**2/4-F*C_g/2
		x_plot.append(C_m)
		y_plot_1.append(R_l_1)
		y_plot_2.append(R_h)

	plt.figure(4)
	plt.plot(x_plot, y_plot_1, label = r'$C_g = 2.0$, with electricity Option I', marker = 'o', fillstyle = 'none')
	plt.plot(x_plot, y_plot_2, label = r'$C_g = 2.0$, w/o electricity Option I', marker = '^', fillstyle = 'none')
	plt.legend()
	plt.xlabel('Price of electricity from Option I, ' + r'$C_m$')
	plt.ylabel('Highest Expected Profit, '+ r'$R_I$')
	plt.xlim([0.2,C_g/2])
	plt.grid(True)
	plt.savefig('figure6.png')

if __name__ == '__main__':
	intialize_customer_array()
	calculate_F_and_G()
	plot_E_m_vary_C_m_keeping_C_m_constant()
	plot_E_g_vary_beta_keeping_C_g_C_m_constant()
	plot_p_vary_beta_keeping_C_g_C_m_constant()
	plot_profit_vary_C_m_keeping_C_g_constant()
	plt.show()