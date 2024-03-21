import { Entity, Column, PrimaryGeneratedColumn } from "typeorm"

@Entity()
export class Exams {
    @PrimaryGeneratedColumn()
    id!: number;

    @Column()
    students!: [number];

    @Column()
    grade!: string;
}


Teacher - id, surname, name, classes, email
Students - id, surname, name, class, teachers, parents_mail, exams, personal_rating
Student_class - id, students, classes
