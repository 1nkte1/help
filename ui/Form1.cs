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

namespace ui
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
            LoadData();
        }

        private void LoadData()
        {
            // путь к бд
            string config = "Data Source=materials.db;Version=3";
            // подключение к бд
            using (var connection = new SQLiteConnection(config))
            {
                connection.Open();

                string query = @"
                    SELECT
                    mt.material_type,
                    mn.material_name,
                    m.min_quantity,
                    m.quantity,
                    m.price,
                    m.pack_size,
                    m.unit
                    FROM materials m
                    JOIN material_types mt ON m.material_type_id = mt.id
                    JOIN material_names mn ON m.material_name_id = mn.id
                ";

                using (var command = new SQLiteCommand(query, connection))
                using (var reader = command.ExecuteReader())
                {
                    while (reader.Read())
                    {
                        string type = reader.GetString(0);
                        string name = reader.GetString(1);
                        int minQuantity = reader.GetInt32(2);
                        int quantity = reader.GetInt32(3);
                        double price = reader.GetDouble(4);
                        int packSize = reader.GetInt32(5);
                        string unit = reader.GetString(6);

                        AddData(type, name, minQuantity, quantity, price, packSize, unit);
                    }
                }
            }
        }

        private void AddData(string type, string name, int minQuantity, int quantity, double price, int packSize, string unit)
        {
            // цена 1 упаковки, округляем до 2 знаков после запятой
            double packCost = Math.Round(packSize * price, 2);
            double neededPacks, cost;

            // если на складе меньше чем необходимое количество
            if (quantity - minQuantity < 0)
            {
                int neededQuantity = minQuantity - quantity;
                neededPacks = Math.Ceiling((double)neededQuantity / packSize);
            }
            else
            {
                neededPacks = Math.Ceiling((double)minQuantity / packSize);
            }
            cost = Math.Round(neededPacks * packCost, 2);


            Panel card = new Panel()
            {
                Width = 700,
                Height = 120,
                BorderStyle = BorderStyle.FixedSingle,
                BackColor = ColorTranslator.FromHtml("#ABCFCE"),
            };

            Label titleLabel = new Label()
            {
                Text = $"{type} | {name}",
                Font = new Font("Comic Sans MS", 14),
                AutoSize = true,
            };
            card.Controls.Add(titleLabel);

            Label minQuantityLabel = new Label();
            minQuantityLabel.Text = $"Минимальное количество: {minQuantity} {unit}";

            Label quantityLabel = new Label();
            quantityLabel.Text = $"Количество на складе: {quantity} {unit}";

            Label priceUnitLabel = new Label();
            priceUnitLabel.Text = $"Цена: {packCost} р / Единица измерения: {unit}";

            Label costLabel = new Label()
            {
                Text = $"Стоимость партии: {cost} р",
                Font = new Font("Comic Sans MS", 12),
                Top = card.Height / 2,
                Left = card.Width/2,
                AutoSize = true,
            };
            card.Controls.Add(costLabel);

            Label[] labels = { titleLabel, minQuantityLabel, quantityLabel, priceUnitLabel };
            int positionY = 10;
            foreach (Label label in labels)
            {
                label.Top = positionY;
                label.Left = 10;
                label.AutoSize = true;
                card.Controls.Add(label);
                positionY += 25;
            }

            flowLayoutPanel1.Controls.Add(card);
            flowLayoutPanel1.AutoScroll = true;
        }

        private void flowLayoutPanel1_Paint(object sender, PaintEventArgs e)
        {

        }

        private void pictureBox1_Click(object sender, EventArgs e)
        {

        }

        private void label1_Click(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            AddEditForm form = new AddEditForm();
            if (form.ShowDialog() == DialogResult.OK)
            {
                flowLayoutPanel1.Controls.Clear();
                LoadData();
            }
        }
    }
}
