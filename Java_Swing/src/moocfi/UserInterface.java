package moocfi;

import java.awt.BorderLayout;
import java.awt.Container;
import java.awt.Dimension;
import java.awt.GridLayout;

import javax.swing.BoxLayout;
import javax.swing.ButtonGroup;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JRadioButton;
import javax.swing.JTextArea;
import javax.swing.JTextField;
import javax.swing.WindowConstants;

import com.sun.org.apache.bcel.internal.generic.NEW;


public class UserInterface implements Runnable {
	
	private JFrame frame;
	
	public UserInterface() {
		
	}
	
	@Override
	public void run() {
		frame = new JFrame("Title");
		frame.setPreferredSize(new Dimension(400, 400));
		
		frame.setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE);
		
		createComponents(frame.getContentPane());
		
		frame.pack();
		frame.setVisible(true);
	}
	
	private void createComponents(Container container) {
		
		GridLayout layout = new GridLayout(3, 2);
        container.setLayout(layout);

        JLabel textName = new JLabel("Name: ");
        JTextField nameField = new JTextField();
        JLabel textID = new JLabel("ID: ");
        JTextField idField = new JTextField();

        JButton addButton = new JButton("Add!");

        container.add(textName);
        container.add(nameField);
        container.add(textID);
        container.add(idField);
        container.add(new JLabel(""));
        container.add(addButton);
        
		/*GridLayout layout = new GridLayout(1, 3);
		container.setLayout(layout);
		JTextArea textAreaLeft = new JTextArea("The Copier");
		JTextArea textAreaRight = new JTextArea();
		JButton copyButton = new JButton("Copy!");
		AreaCopier copier = new AreaCopier(textAreaLeft, textAreaRight);
		copyButton.addActionListener(copier);
		container.add(textAreaLeft);
		container.add(copyButton);
		container.add(textAreaRight);*/
				
		/*BoxLayout layout = new BoxLayout(container, BoxLayout.X_AXIS);
		container.setLayout(layout);
		container.add(new JLabel("Choose meat or fish:"));
		JRadioButton meat = new JRadioButton("Meat");
		JRadioButton fish = new JRadioButton("Fish");
		meat.setSelected(true);
		ButtonGroup buttonGroup = new ButtonGroup();
		buttonGroup.add(meat);
		buttonGroup.add(fish);
		container.add(meat);
		container.add(fish);

		JButton button = new JButton("Send!");
		button.addActionListener(new MessageListener());
		container.add(button);*/
		
		
		/*BoxLayout layout = new BoxLayout(container, BoxLayout.Y_AXIS);
		// BoxLayout layout = new BoxLayout(container, BoxLayout.X_AXIS);
		container.setLayout(layout);
		container.add(new JLabel("First!"));
		container.add(new JLabel("Second!"));
		container.add(new JLabel("Third!"));*/
		
		/*container.add(new JButton("North"), BorderLayout.NORTH);
		container.add(new JButton("East"), BorderLayout.EAST);
		container.add(new JButton("South"), BorderLayout.SOUTH);
		container.add(new JButton("West"), BorderLayout.WEST);
		container.add(new JButton("Default (Center)"));*/
		
		/*JLabel text = new JLabel("Text Field");
		container.add(text);
		JButton button = new JButton("Click me!");
		container.add(button);*/
	}
	
	public JFrame getFrame() {
		return frame;
	}
	
}
