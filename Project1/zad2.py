import zestaw1

if __name__ == "__main__":
    adj_list = zestaw1.gen_G_p(6, 0.7)
    zestaw1.create_file_to_draw(adj_list)
    zestaw1.draw_circular(adj_list)