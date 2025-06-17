using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Data.SQLite;
using System.Xml;

namespace ui
{
    public partial class AddEditForm : Form
    {
        private int? materialId = null;

        public AddEditForm(int? id = null)
        {
            InitializeComponent();
            materialId = id;

            if (materialId == null)
            {
                label1.Text = "Добавление новой записи";
            }
            else
            {
                label1.Text = "Редактирование записи";
            }
        }

        private void LoadMaterialTypes()
        {
            string config = "Data Source=materials.db;Version=3;";
            using (var connection = new SQLiteConnection(config))
            {
                connection.Open();

                string query = @"
                SELECT id, material_type 
                FROM material_types
                ";

                SQLiteDataAdapter adapter = new SQLiteDataAdapter(query, connection);
                DataTable table = new DataTable();
                adapter.Fill(table);

                comboBox1.DataSource = table;
                comboBox1.DisplayMember = "material_type";
                comboBox1.ValueMember = "id";
            }

        }

        private void Validate()
        {
            string name, unit;
            int typeId, quantity, packSize, minQuantity;
            double price;

            if (string.IsNullOrWhiteSpace(textBox1.Text))
            {
                MessageBox.Show("Введите наименование материала", "Ошибка", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }
            name = textBox1.Text;
            typeId = Convert.ToInt32(comboBox1.SelectedValue);

            if (int.TryParse(textBox2.Text, out int textBox2Value))
            {
                if (textBox2Value < 0)
                {
                    MessageBox.Show("Количество складе не может быть отрицательным", "Ошибка", MessageBoxButtons.OK, MessageBoxIcon.Error);
                    return;
                }
                quantity = textBox2Value;
            }
            else
            {
                MessageBox.Show("Количество материала должно быть целым числом", "Ошибка", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }

            if (string.IsNullOrWhiteSpace(textBox3.Text))
            {
                MessageBox.Show("Введите единицу измерения", "Ошибка", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }
            unit = textBox3.Text;


            if (int.TryParse(textBox4.Text, out int textBox4Value))
            {
                if (textBox4Value < 0)
                {
                    MessageBox.Show("Количество в упаковке не может быть отрицательным", "Ошибка", MessageBoxButtons.OK, MessageBoxIcon.Error);
                    return;
                }
                packSize = textBox4Value;
            }
            else
            {
                MessageBox.Show("Количество в упаковке должно быть целым числом", "Ошибка", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }

            if (int.TryParse(textBox5.Text, out int textBox5Value))
            {
                if (textBox5Value < 0)
                {
                    MessageBox.Show("Минимальное количество не может быть отрицательным", "Ошибка", MessageBoxButtons.OK, MessageBoxIcon.Error);
                    return;
                }
                minQuantity = textBox5Value;
            }
            else
            {
                MessageBox.Show("Минимальное количество должно быть целым числом", "Ошибка", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }

            if (double.TryParse(textBox6.Text, out double textBox6Value))
            {
                if (textBox6Value < 0)
                {
                    MessageBox.Show("Цена не может быть отрицательной", "Ошибка", MessageBoxButtons.OK, MessageBoxIcon.Error);
                    return;
                }
                price = Math.Round(textBox6Value, 2);
                textBox6.Text = price.ToString();
            }
            else
            {
                MessageBox.Show("Цена дожна быть числом", "Ошибка", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }
            Add(name, typeId, quantity, unit, packSize, minQuantity, price);
            MessageBox.Show("Материал успешно добавлен!", "Оповещение", MessageBoxButtons.OK, MessageBoxIcon.Information);
            textBox1.Text = "";
            textBox2.Text = "";
            textBox3.Text = "";
            textBox4.Text = "";
            textBox5.Text = "";
            textBox6.Text = "";
        }

        private void Add(string name, int typeId, int quantity, string unit, int packSize, int minQuantity, double price)
        {
            string config = "Data Source=materials.db;Version:3;";
            using (var connection = new SQLiteConnection(config))
            {
                connection.Open();

                string query = "SELECT id FROM material_names WHERE material_name == @name";
                using (var command = new SQLiteCommand(query, connection))
                {
                    command.Parameters.AddWithValue("name", name);
                }



//                string query = @"
//INSERT INTO materials AS m
//(
//material_type_id,
//material_name,
//price,
//quantity,
//min_quantity,
//pack_size,
//unit
//)
//VALUES
//()
//JOIN material_names AS mn ON m.material_name_id == mn.id
//                ";
            }
        }



        private void AddEditForm_Load(object sender, EventArgs e)
        {
            if (materialId == null)
                LoadMaterialTypes();
            else
                EditPlaceholder();
        }

        private void EditPlaceholder()
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {

        }

        private void label1_Click(object sender, EventArgs e)
        {

        }

        private void label3_Click(object sender, EventArgs e)
        {

        }

        private void textBox1_TextChanged(object sender, EventArgs e)
        {

        }

        private void label2_Click(object sender, EventArgs e)
        {

        }

        private void comboBox1_SelectedIndexChanged(object sender, EventArgs e)
        {

        }

        private void label6_Click(object sender, EventArgs e)
        {

        }

        private void button2_Click(object sender, EventArgs e)
        {
            Validate();
        }
    }
}
